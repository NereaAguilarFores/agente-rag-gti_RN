import json
from pathlib import Path

RUNS = {
    "llama3.2:3b": "benchmark/runs/run_20260519_044702.json",
    "qwen2.5:3b": "benchmark/runs/run_20260529_200230.json",
    "poligpt": "benchmark/runs/run_20260529_213841.json",
    "qwen": "benchmark/runs/run_20260529_215142.json",
}

GROUND_TRUTH = {
    "q1": "DNI es una asociación juvenil de voluntariado en Valencia que desarrolla proyectos sociales como desayunos solidarios, actividades con personas mayores y refuerzo escolar.",
    "q2": "Para apuntarse a los desayunos solidarios hay que esperar al miércoles, cuando se publica el formulario de inscripción por la comunidad de WhatsApp y redes sociales. Es una actividad puntual y no obliga a asistir siempre.",
    "q3": "COLES es refuerzo escolar con niños en situación vulnerable, con actividades como repaso, lectura y manualidades. RESIS consiste en actividades y acompañamiento con personas mayores en la residencia L'Acollida.",
    "q4": "En el refuerzo escolar se ayuda a niños que viven realidades difíciles mediante repaso de deberes o conceptos, lectura de cuentos y manualidades.",
    "q5": "Las actividades con los abuelitos se realizan los miércoles de 17:30 a 18:30 en la residencia L'Acollida.",
    "q6": "La diferencia principal es la hora y los alimentos: en desayunos se lleva café, zumos y bollería; en cenas, bocadillos y fruta.",
    "q7": "No tengo esa información en mis fuentes.",
    "q8": "No tengo esa información en mis fuentes.",
}


def overlap_score(texto, referencia):
    texto_words = set(texto.lower().replace(".", "").replace(",", "").split())
    ref_words = set(referencia.lower().replace(".", "").replace(",", "").split())
    if not ref_words:
        return 0.0
    return round(len(texto_words & ref_words) / len(ref_words), 3)


def source_precision(fuentes, esperadas):
    if not fuentes:
        return 0.0
    if not esperadas:
        return 1.0
    correctas = len(set(fuentes) & set(esperadas))
    return round(correctas / len(fuentes), 3)


def source_recall(fuentes, esperadas):
    if not esperadas:
        return 1.0
    correctas = len(set(fuentes) & set(esperadas))
    return round(correctas / len(esperadas), 3)


def rejection_ok(item):
    if item["categoria"] != "fuera_de_ambito":
        return None
    respuesta = item["salida"]["respuesta"].lower()
    return "no tengo esa información en mis fuentes" in respuesta


def evaluar_item(item):
    salida = item["salida"]
    respuesta = salida["respuesta"]
    chunks = salida.get("chunks", [])
    contexto = " ".join(ch.get("text", "") for ch in chunks)
    fuentes = salida.get("fuentes", [])
    esperadas = item.get("fuentes_esperadas", [])
    gt = GROUND_TRUTH[item["id"]]

    return {
        "id": item["id"],
        "pregunta": item["pregunta"],
        "categoria": item["categoria"],
        "respuesta": respuesta,
        "ground_truth": gt,
        "ragas": {
            "faithfulness": overlap_score(respuesta, contexto),
            "answer_relevancy": overlap_score(respuesta, gt),
            "context_precision": source_precision(fuentes, esperadas),
            "context_recall": source_recall(fuentes, esperadas),
        },
        "metricas_propias": {
            "precision_fuentes_esperadas": source_recall(fuentes, esperadas),
            "rechazo_fuera_de_ambito_correcto": rejection_ok(item),
        },
    }


def main():
    resultados = {}

    for modelo, ruta in RUNS.items():
        datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
        evaluados = [evaluar_item(item) for item in datos]

        medias = {}
        for metrica in ["faithfulness", "answer_relevancy", "context_precision", "context_recall"]:
            valores = [x["ragas"][metrica] for x in evaluados]
            medias[metrica] = round(sum(valores) / len(valores), 3)

        resultados[modelo] = {
            "num_preguntas": len(evaluados),
            "resultados_por_pregunta": evaluados,
            "medias_ragas": medias,
        }

    Path("evaluacion").mkdir(exist_ok=True)
    Path("evaluacion/ragas_results.json").write_text(
        json.dumps(resultados, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("OK: generado evaluacion/ragas_results.json")


if __name__ == "__main__":
    main()
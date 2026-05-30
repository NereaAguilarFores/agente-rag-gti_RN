"""Evaluacion heuristica reproducible para Banda 8.

Este script no sustituye a una ejecucion completa de la libreria RAGAs con LLM
juez, pero permite recalcular una aproximacion determinista cuando existan los
JSON crudos de benchmark/runs. Usa las mismas definiciones generales:
faithfulness, answer_relevancy, context_precision y context_recall.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark" / "benchmark.json"
QUESTIONS = ROOT / "benchmark" / "preguntas.json"
GROUND_TRUTH = ROOT / "evaluacion" / "ground_truth.json"
OUT = ROOT / "evaluacion" / "ragas_results_recalculado.json"
REJECTION = "No tengo esa información en mis fuentes"


def _tokens(text: str) -> set[str]:
    return {
        t
        for t in re.findall(r"[a-záéíóúüñ0-9]+", text.lower())
        if len(t) > 3
    }


def _overlap(a: str, b: str) -> float:
    ta = _tokens(a)
    tb = _tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(tb)


def _clip(x: float) -> float:
    return round(max(0.0, min(1.0, x)), 3)


def evaluate_run(run_path: Path, questions: dict, ground_truth: dict) -> dict:
    rows = json.loads(run_path.read_text(encoding="utf-8"))
    per_question = []

    for row in rows:
        qid = row["id"]
        expected_sources = set(questions[qid].get("fuentes_esperadas", []))
        reference = ground_truth[qid]["respuesta_referencia"]
        salida = row.get("salida", {})

        answer = salida.get("respuesta", "") if isinstance(salida, dict) else ""
        chunks = salida.get("chunks", []) if isinstance(salida, dict) else []
        fuentes = set(salida.get("fuentes", [])) if isinstance(salida, dict) else set()
        context_text = "\n".join(c.get("text", "") for c in chunks if isinstance(c, dict))
        chunk_sources = {c.get("source") for c in chunks if isinstance(c, dict)}

        if not expected_sources:
            rejected = REJECTION.lower() in answer.lower()
            faithfulness = 1.0 if rejected else 0.2
            answer_relevancy = 1.0 if rejected else 0.2
            context_precision = 1.0 if rejected else 0.3
            context_recall = 1.0 if rejected else 0.3
        else:
            found = expected_sources & (fuentes | chunk_sources)
            source_coverage = len(found) / len(expected_sources)
            answer_relevancy = _overlap(answer, reference)
            context_recall = source_coverage
            context_precision = len(found) / max(1, len(chunk_sources))
            faithfulness = 0.5 * _overlap(answer, context_text) + 0.5 * source_coverage

        per_question.append(
            {
                "id": qid,
                "faithfulness": _clip(faithfulness),
                "answer_relevancy": _clip(answer_relevancy),
                "context_precision": _clip(context_precision),
                "context_recall": _clip(context_recall),
            }
        )

    averages = {
        key: round(sum(x[key] for x in per_question) / len(per_question), 3)
        for key in ("faithfulness", "answer_relevancy", "context_precision", "context_recall")
    }
    return {"run": str(run_path.relative_to(ROOT)), "promedios": averages, "preguntas": per_question}


def main() -> int:
    benchmark = json.loads(BENCHMARK.read_text(encoding="utf-8"))
    questions = {q["id"]: q for q in json.loads(QUESTIONS.read_text(encoding="utf-8"))}
    ground_truth = {q["id"]: q for q in json.loads(GROUND_TRUTH.read_text(encoding="utf-8"))}

    results = []
    missing = []
    for model in benchmark["modelos_evaluados"]:
        run_path = ROOT / "benchmark" / model["resultado"]
        if not run_path.exists():
            missing.append(str(run_path.relative_to(ROOT)))
            continue
        evaluated = evaluate_run(run_path, questions, ground_truth)
        evaluated["modelo"] = model["alias"]
        evaluated["servidor"] = model["servidor"]
        results.append(evaluated)

    OUT.write_text(
        json.dumps(
            {
                "metodologia": "heuristica_reproducible_sobre_runs_crudos",
                "runs_evaluados": results,
                "runs_no_encontrados": missing,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Resultados escritos en {OUT}")
    if missing:
        print("Runs no encontrados:")
        for item in missing:
            print(f"- {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Benchmark

Esta carpeta recoge el benchmark usado para comparar el agente RAG de DNI Valencia con cuatro modelos distintos.

## Objetivo

El benchmark valida:

- Calidad factual de las respuestas.
- Capacidad de citar fuentes del corpus.
- Comportamiento anti-alucinacion ante preguntas fuera de ambito.
- Latencia y velocidad de generacion.
- Diferencias entre modelos locales y modelos PoliGPT.

## Archivos

- `preguntas.json`: conjunto fijo de preguntas.
- `benchmark.json`: resumen estructurado de modelos evaluados y rutas de resultados.
- `benchmark.md`: resultados narrativos y conclusiones por modelo.
- `benchmark_resultados.md`: copia de trabajo con el analisis completo.

Nota: `benchmark.json` referencia ficheros `runs/run_*.json`. Si esos ficheros existen fuera del repositorio, deben incorporarse antes de entregar o actualizarse las referencias para que apunten a archivos presentes.

## Preguntas

El set actual contiene 8 preguntas:

- Preguntas generales sobre DNI.
- Preguntas sobre desayunos solidarios.
- Preguntas comparativas entre RESIS y COLES.
- Preguntas sobre refuerzo escolar y residencias.
- Dos preguntas fuera de ambito que deben rechazarse.

## Modelos comparados

| Modelo | Entorno | Observacion principal |
|---|---|---|
| `llama3.2:3b` | Ollama local | Rapido y suficiente para preguntas directas; mas limitado en sintesis compleja. |
| `qwen2.5:3b` | Ollama local | Buen equilibrio entre velocidad, respuesta en espanol y sintesis. |
| `poligpt` | PoliGPT UPV | Respuestas mas completas y estructuradas, con mayor latencia. |
| `qwen` | PoliGPT UPV | Buena calidad en comparativas, pero respuestas largas y latencia elevada. |

## Metricas registradas

Cada ejecucion del agente devuelve:

- `prompt_tokens`.
- `output_tokens`.
- `tokens_per_sec`.
- `latencia_s`.
- `modelo`.
- fuentes recuperadas.
- chunks usados.
- respuesta generada.

Ademas, se realizo una valoracion cualitativa de acierto, rechazo correcto y problemas observados.

## Ejecucion

```bash
python scripts/run_eval.py
```

El script genera un archivo JSON dentro de `benchmark/runs/` con timestamp. Para que la entrega sea reproducible, conviene conservar esos JSON o ajustar `benchmark.json` a las rutas existentes.

## Resultados

El analisis completo esta en:

- `benchmark.md`
- `benchmark_resultados.md`

Conclusion resumida:

- PoliGPT ofrece mejor sintesis, pero con mas coste temporal.
- `qwen2.5:3b` es la opcion local mas equilibrada.
- El control anti-alucinacion funciona bien en preguntas fuera de ambito.
- Persisten rechazos innecesarios en alguna pregunta general como "Que es DNI?".

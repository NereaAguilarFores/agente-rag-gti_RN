# Evaluación Banda 8

Esta carpeta contiene la evaluación adicional requerida para Banda 8:

- `ragas_results.json`: resultados de las cuatro métricas RAGAs solicitadas.
- `metricas_propias.md`: definicion, justificacion y valores de dos métricas propias.
- `ground_truth.json`: respuestas de referencia usadas para comparar el benchmark.
- `run_ragas_eval.py`: script preparado para recalcular la evaluacion si se incorporan los JSON crudos de `benchmark/runs/`.

## Importante sobre la metodologia

Los ficheros de `benchmark/runs/` para los cuatro modelos son runs reales. Los modelos locales (`llama3.2:3b` y `qwen2.5:3b`) se generaron de nuevo con Ollama el 2026-05-30. Los ficheros de PoliGPT (`poligpt` y `qwen`) se incorporaron desde los resultados guardados por el equipo.

Los resultados incluidos en `ragas_results.json` se han consolidado como evaluacion manual con rúbrica RAGAs a partir de:

- el benchmark documentado en `benchmark/benchmark.md`;
- las observaciones de las pruebas iterativas de `pruebas/`;
- las fuentes esperadas de `benchmark/preguntas.json`;
- las respuestas de referencia de `ground_truth.json`.

Las métricas mantienen las definiciónes de RAGAs:

- `faithfulness`: fidelidad de la respuesta al contexto recuperado.
- `answer_relevancy`: grado en que la respuesta contesta a la pregunta.
- `context_precision`: proporcion de chunks recuperados utiles.
- `context_recall`: proporción de información necesaria presente en los chunks.

Además, `ragas_results_recalculado.json` contiene una evaluacion heurística reproducible calculada sobre los runs presentes.

Si se sustituyen los JSON por nuevas ejecuciónes, debe ejecutarse:

```bash
python evaluacion/run_ragas_eval.py
```

Ese script recalcula métricas heurísticas reproducibles usando las fuentes esperadas y las respuestas de referencia.

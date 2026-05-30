# Registro de pruebas

Esta carpeta conserva el historial de pruebas realizadas durante el desarrollo del agente RAG. No forma parte del contrato principal del corrector, pero sirve como evidencia de las decisiones tomadas y como base para el informe.

## Orden recomendado de lectura

1. `pruebas_iniciales.md`: primeras ejecuciones y problemas detectados.
2. `pruebas_iterativas_rag_segunda_prueba.md`: corrección del rol del asistente, prompt anti-alucinación y aumento de top-k.
3. `pruebas_query_expansion_tercera_prueba.md`: expansion de consultas para mejorar recuperacion.
4. `pruebas_generalizaciones_prompt_cuarta_prueba.md`: reglas para evitar generalizaciones.
5. `pruebas_sintesis_cuarta_prueba.md`: mejora de síntesis de informacion multi-documento.
6. `pruebas_formato_comparativo_quinta_prueba.md`: formato comparativo para RESIS y COLES.
7. `pruebas_siglas_acronimos_sexta_prueba.md`: evitar inventar significados de siglas.
8. `pruebas_regla_resis_coles_septima_prueba.md`: regla especifica para diferenciar RESIS y COLES.
9. `pruebas_uso_datos_contexto_octava_prueba.md`: uso prioritario de datos presentes en contexto.
10. `pruebas_benchmark_qwen25_novena_prueba.md` y `benchmark_modelo_qwen25.md`: evaluacion con `qwen2.5:3b`.
11. `pruebas_poligpt_decima_prueba.md`: evaluacion con PoliGPT.
12. `pruebas_qwen_poligpt_undecima_prueba.md`: evaluacion con `qwen` en PoliGPT.

## Cambios principales derivados de las pruebas

- Se adapto el rol del asistente al caso DNI Valencia.
- Se reforzó el rechazo de preguntas fuera de ámbito.
- Se aumento el numero de chunks recuperados para preguntas comparativas.
- Se anadio expansion de consulta para RESIS y COLES.
- Se incorporaron reglas para no inventar significados de siglas.
- Se mejoro el formato de respuestas comparativas.
- Se compararon modelos locales y PoliGPT para seleccionar el comportamiento más equilibrado.

## Aviso

Algunos archivos conservan salidas antiguas donde el sistema fallaba o inventaba información. Se mantienen como evidencia del proceso iterativo, no como resultado final del agente.

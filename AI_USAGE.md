# Uso de asistentes de IA

Este documento declara de forma honesta las herramientas de IA usadas durante la practica y en que partes ayudaron. Todo el codigo y la documentacion entregados han sido revisados por las integrantes del grupo.

## Herramientas usadas

- [X] ChatGPT / Codex.
- [ ] Claude.
- [ ] GitHub Copilot.
- [ ] Cursor / Windsurf / IDE con asistente integrado.
- [ ] Gemini.
- [X] Ollama local con modelos abiertos.
- [X] PoliGPT UPV para evaluacion comparativa.
- [ ] Otras.

## Uso de ChatGPT / Codex

ChatGPT/Codex se uso como apoyo en:

- Comprension de la estructura del agente RAG: separacion entre `chunker`, `retriever`, `generator`, `prompts` y `pipeline`.
- Revision de errores de ejecucion e instalacion de dependencias.
- Ayuda para redactar y reorganizar documentacion de entrega.
- Apoyo en la interpretacion de resultados de pruebas y benchmark.
- Revision de referencias antiguas de la plantilla original para adaptarlas al caso DNI Valencia.

Las propuestas generadas por IA fueron revisadas manualmente antes de incorporarse al proyecto.

## Uso de Ollama local

Ollama se uso para:

- Generar embeddings mediante `nomic-embed-text`.
- Ejecutar modelos locales para responder preguntas del agente.
- Evaluar modelos locales en el benchmark, especialmente `llama3.2:3b` y `qwen2.5:3b`.

## Uso de PoliGPT

PoliGPT se uso para comparar el comportamiento del sistema con modelos externos disponibles en la infraestructura UPV:

- `poligpt`.
- `qwen`.

Se registraron resultados de calidad, latencia, tokens de entrada/salida y observaciones cualitativas.

## Partes revisadas por el grupo

- Prompt anti-alucinacion.
- Respuestas sobre RESIS, COLES y desayunos solidarios.
- Ficheros de benchmark.
- Documentacion obligatoria de entrega.
- Declaracion de bandas en `features.json`.

## No usado para

- No se uso IA para inventar resultados de benchmark.
- No se uso IA para inventar resultados RAGAs.
- No se uso IA para modificar el corpus oficial.
- No se subieron claves privadas ni secretos a asistentes externos.

## Compromiso

Hemos leido y entendido el codigo y la documentacion que entregamos. En la defensa oral podremos explicar el flujo del agente, las decisiones tomadas y las limitaciones del sistema.

Firma digital:

- Nerea Aguilar Fores.
- Judit Espinoza Cervera.

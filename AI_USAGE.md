# Uso de asistentes de IA

Este documento declara de forma honesta las herramientas de IA usadas durante la práctica y en qué partes ayudaron. Todo el código y la documentación entregados han sido revisados por las integrantes del grupo.

## Herramientas usadas

- [X] ChatGPT / Codex.
- [ ] Claude.
- [ ] GitHub Copilot.
- [ ] Cursor / Windsurf / IDE con asistente integrado.
- [ ] Gemini.
- [X] Ollama local con modelos abiertos.
- [X] PoliGPT UPV para evaluación comparativa.
- [ ] Otras.

## Uso de ChatGPT / Codex

ChatGPT/Codex se uso como apoyo en:

- Comprension de la estructura del agente RAG: separacion entre `chunker`, `retriever`, `generator`, `prompts` y `pipeline`.
- Revisión de errores de ejecución e instalación de dependencias.
- Ayuda para redactar y reorganizar documentación de entrega.
- Apoyo en la interpretación de resultados de pruebas y benchmark.
- Revisión de referencias antiguas de la plantilla original para adaptarlas al caso DNI Valencia.

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

- Prompt anti-alucinación.
- Respuestas sobre RESIS, COLES y desayunos solidarios.
- Ficheros de benchmark.
- Documentación obligatoria de entrega.
- Declaracion de bandas en `features.json`.

## No usado para

- No se uso IA para inventar resultados de benchmark.
- No se uso IA para inventar resultados RAGAs.
- No se uso IA para modificar el corpus oficial.
- No se subieron claves privadas ni secretos a asistentes externos.

## Compromiso

Hemos leído y entendido el código y la documentación que entregamos. En la defensa oral podremos explicar el flujo del agente, las decisiones tomadas y las limitaciones del sistema.

Firma digital:

- Nerea Aguilar Fores.
- Judit Espinoza Cervera.

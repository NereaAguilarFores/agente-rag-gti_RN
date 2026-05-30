# Arquitectura y decisiones técnicas

## Arquitectura elegida

El proyecto usa una arquitectura single-agent modular. No es una arquitectura hexagonal completa, pero separa las responsabilidades principales del sistema RAG en módulos independientes:

- `chunker.py`: carga y trocea los documentos del corpus.
- `embedder.py`: genera embeddings.
- `retriever.py`: consulta ChromaDB y devuelve chunks relevantes.
- `prompts.py`: construye el prompt final.
- `generator.py`: llama al modelo generador.
- `pipeline.py`: orquesta el flujo completo de consulta.

Esta decision permite mantener el proyecto sencillo y compatible con el contrato de la práctica, sin asumir el coste de reestructuracion necesario para Banda 10.

## Flujo de indexacion

1. `scripts/build_index.py` carga los documentos de `corpus/`.
2. `chunker.load_corpus` lee los `.txt`.
3. `chunker.split_documents` divide los textos en chunks.
4. `retriever.build_index` calcula embeddings y los guarda en ChromaDB.
5. El indice se persiste en disco para no recalcularlo en cada consulta.

## Flujo de consulta

1. El corrector o usuario llama a `consultar(pregunta)`.
2. `pipeline.answer` recibe la pregunta.
3. `retriever.retrieve` recupera los chunks mas similares.
4. `prompts.build_prompt` crea un prompt con reglas anti-alucinacion.
5. `generator.generate` llama al LLM configurado.
6. El sistema devuelve respuesta, fuentes, chunks, métricas y trazas.

## Chunking

Se usa `RecursiveCharacterTextSplitter` con:

- `chunk_size=500`.
- `chunk_overlap=100`.

Esta configuración busca equilibrar:

- contexto suficiente para responder preguntas complejas;
- prompts no excesivamente largos;
- trazabilidad clara al archivo origen.

Los nombres de archivo se conservan como metadatos para poder citar fuentes en la respuesta final.

## Vector store

Se usa ChromaDB persistente. La persistencia evita recalcular embeddings cada vez que se ejecuta el agente y mejora la experiencia durante la defensa oral.

La coleccion usa similitud coseno. Internamente ChromaDB devuelve distancias, y el sistema las transforma en `score = 1 - distance` para que valores mas altos indiquen mayor similitud.

## Prompt anti-alucinación

El prompt obliga al modelo a:

- responder solo con información del contexto;
- rechazar preguntas fuera de ámbito;
- citar siempre el archivo fuente;
- no inventar datos numéricos;
- no inventar significados de siglas;
- tratar RESIS y COLES según lo que aparece en el corpus.

Durante las pruebas se reforzaron reglas especificas para evitar errores detectados en comparativas y siglas.

## Modelos

El sistema puede usar:

- Ollama local, obligatorio para cumplir el minimo de la practica.
- PoliGPT UPV, usado para comparación en benchmark.

El backend se selecciona con variables de entorno. La lógica del pipeline se mantiene igual para comparar modelos de forma justa.

## Métricas

Cada respuesta incluye:

- tokens de entrada;
- tokens de salida;
- tokens por segundo;
- latencia;
- modelo usado.

Estas métricas permiten comparar rendimiento entre modelos en el benchmark.

## Limitaciones

- No hay arquitectura hexagonal con ports y adapters.
- No se implementa retrieval hibrido BM25 + semántico.
- No hay re-ranking.
- No hay memoria conversacional real, aunque el contrato acepta `conversation_id`.
- La evaluación RAGAs de Banda 8 esta documentada en `evaluacion/` como evaluacion manual consolidada.

## Mejoras futuras

- Migrar a arquitectura hexagonal si se aspira a Banda 10.
- Añadir BM25 o re-ranking para mejorar recuperación.
- Agrupar mejor pares `Q:/A:` antes del chunking.
- Recalcular RAGAs con los JSON crudos de `benchmark/runs/` si se recuperan antes de la entrega.
- Crear un frontend sencillo con Streamlit o Gradio como extra.

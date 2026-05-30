# Agente RAG para DNI Valencia

Proyecto de la práctica de Inteligencia Artificial: un agente RAG que responde preguntas sobre la asociación DNI Valencia usando el corpus oficial de 16 ficheros de texto.

El sistema recupera fragmentos relevantes del corpus, construye un prompt con contexto, genera una respuesta con un LLM y devuelve siempre las fuentes usadas. Cuando la informacion no aparece en el corpus, debe responder con la frase de rechazo configurada: `No tengo esa informacion en mis fuentes`.

## Estado de la entrega

Capacidades documentadas en esta versión:

- Banda 5: pipeline RAG completo con chunking, embeddings, vector store, retrieval, LLM y prompt anti-alucinación.
- Banda 6: cita de archivos fuente en cada respuesta.
- Banda 7: benchmark comparativo con 4 modelos: `llama3.2:3b`, `qwen2.5:3b`, `poligpt` y `qwen`.
- Banda 8: evaluación RAGAs documentada y dos métricas propias en `evaluacion/`.
- Banda 10: no implementada; la arquitectura actual es single-agent modular, no hexagonal.

El fichero [features.json](features.json) declara las bandas que se entregan realmente.

## Requisitos

- Python 3.11 o superior.
- Ollama instalado y en ejecucion.
- Modelo de embeddings `nomic-embed-text`.
- Al menos un modelo local para consultas, por ejemplo `llama3.2:3b` o `qwen2.5:3b`.
- Para benchmark con PoliGPT: clave de API y VPN/red UPV cuando sea necesario.

Instalacion recomendada:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
ollama pull nomic-embed-text
ollama pull llama3.2:3b
ollama pull qwen2.5:3b
```

## Configuración

Copiar `.env.example` a `.env` si se quiere cambiar la configuracion por defecto:

```bash
copy .env.example .env
```

Variables principales:

- `OLLAMA_URL`: endpoint de Ollama, por defecto `http://localhost:11434/api`.
- `LLM_MODEL`: modelo generador usado por defecto.
- `EMBED_MODEL`: modelo de embeddings.
- `CHROMA_PATH`: ruta donde se guarda el indice persistente de ChromaDB.
- `COLLECTION_NAME`: nombre de la coleccion vectorial.
- `POLIGPT_BASE_URL`, `POLIGPT_API_KEY` y `POLIGPT_MODEL`: necesarias si se usa PoliGPT.

## Uso

Construir el indice vectorial:

```bash
python scripts/build_index.py
```

Lanzar una consulta desde consola:

```bash
python consultar.py "Como me apunto a los desayunos solidarios?"
```

La función obligatoria del contrato está en la raíz del repositorio:

```python
from consultar import consultar

salida = consultar("En que se diferencian RESIS y COLES?")
```

La salida tiene esta forma:

```json
{
  "respuesta": "Texto de la respuesta con fuente citada.",
  "fuentes": ["06_coles_refuerzo.txt", "16_resis_49_preguntas.txt"],
  "chunks": [
    {
      "source": "06_coles_refuerzo.txt",
      "text": "...",
      "score": 0.82
    }
  ],
  "metricas": {
    "prompt_tokens": 612,
    "output_tokens": 90,
    "tokens_per_sec": 42.1,
    "latencia_s": 2.4,
    "modelo": "llama3.2:3b"
  },
  "trazas": null
}
```

También existe una opción HTTP con FastAPI:

```bash
uvicorn api:app --host 127.0.0.1 --port 8000
```

Endpoint:

```http
POST /query
```

## Estructura

```text
.
|-- consultar.py              # contrato principal de la práctica
|-- api.py                    # endpoint HTTP opcional
|-- features.json             # declaración de bandas y extras
|-- AI_USAGE.md               # uso de IA durante el desarrollo
|-- GRUPO.md                  # integrantes y reparto de trabajo
|-- corpus/                   # 16 documentos oficiales de DNI Valencia
|-- src/agente_rag/           # implementación modular del agente
|   |-- chunker.py            # carga y troceo del corpus
|   |-- embedder.py           # cliente de embeddings
|   |-- retriever.py          # ChromaDB y recuperación semántica
|   |-- prompts.py            # prompt anti-alucinación
|   |-- generator.py          # generación con Ollama o PoliGPT
|   `-- pipeline.py           # orquestación de la consulta
|-- scripts/
|   |-- build_index.py        # genera el índice vectorial
|   `-- run_eval.py           # ejecuta el benchmark
|-- benchmark/                # preguntas y resultados de benchmark
|-- pruebas/                  # registro de pruebas iterativas
|-- docs/                     # arquitectura y contrato
`-- tests/                    # tests unitarios del contrato
```

## Funcionamiento interno

El flujo de una consulta es:

1. El usuario llama a `consultar(pregunta)`.
2. `pipeline.answer` pide al retriever los chunks mas relevantes.
3. `retriever.retrieve` convierte la pregunta en embedding y consulta ChromaDB.
4. `prompts.build_prompt` inserta los chunks recuperados en un prompt con reglas anti-alucinacion.
5. `generator.generate` llama al modelo configurado.
6. El pipeline devuelve respuesta, fuentes, chunks y métricas.

El sistema usa `RecursiveCharacterTextSplitter` con `chunk_size=500` y `chunk_overlap=100`, una configuración recomendada para mantener contexto suficiente sin inflar demasiado el prompt.

## Benchmark

El benchmark usa un conjunto fijo de 8 preguntas, con casos generales, preguntas sobre desayunos, comparaciones entre RESIS y COLES, preguntas de proyectos concretos y preguntas fuera de ámbito.

Modelos evaluados:

- `llama3.2:3b` en Ollama local.
- `qwen2.5:3b` en Ollama local.
- `poligpt` en PoliGPT UPV.
- `qwen` en PoliGPT UPV.

Resultados y análisis:

- [benchmark/benchmark.md](benchmark/benchmark.md)
- [benchmark/benchmark.json](benchmark/benchmark.json)
- [benchmark/preguntas.json](benchmark/preguntas.json)
- [evaluacion/ragas_results.json](evaluacion/ragas_results.json)
- [evaluacion/metricas_propias.md](evaluacion/metricas_propias.md)

La conclusión principal es que los modelos PoliGPT generan respuestas más completas y estructuradas, pero con más latencia; `qwen2.5:3b` ofrece buen equilibrio local; `llama3.2:3b` funciona correctamente pero presenta más limitaciones en síntesis compleja.

## Tests

Los tests comprueban el contrato sin llamar al LLM real:

```bash
pytest -q
```

Nota: el entorno debe tener instaladas todas las dependencias de `requirements.txt`, incluida `openai`, porque el generador soporta también PoliGPT.

## Limitaciones conocidas

- La arquitectura no es hexagonal; el dominio aún depende de módulos concretos de infraestructura.
- El retrieval es semántico con ChromaDB, sin BM25 ni re-ranking.
- El sistema puede ser conservador en preguntas generales cuando el contexto recuperado es parcial.
- Las respuestas de modelos pequeños pueden mezclar información o sintetizar peor en preguntas comparativas.
- Los resultados RAGAs se calculan sobre runs reales de los 4 modelos declarados. Los runs locales se regeneraron con Ollama el 2026-05-30 y los runs PoliGPT se incorporaron desde los resultados guardados por el equipo.

## Documentación adicional

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md): decisiones técnicas.
- [docs/CONTRACT.md](docs/CONTRACT.md): contrato de interfaz.
- [benchmark/README.md](benchmark/README.md): organización del benchmark.
- [evaluacion/ragas_results.json](evaluacion/ragas_results.json): métricas RAGAs consolidadas.
- [evaluacion/metricas_propias.md](evaluacion/metricas_propias.md): dos métricas propias.
- [informe.md](informe.md): informe editable.
- `informe.pdf`: versión PDF para entrega, si se genera desde el informe.

# Resultados benchmark — DNI Valencia

## Configuración

Modelo utilizado:
- llama3.2:3b (Ollama local)

Sistema evaluado:
- Retrieval semántico con ChromaDB
- Embeddings locales
- Prompt anti-alucinación
- Query expansion para preguntas comparativas
- Top-k retrieval = 10

Número de preguntas:
- 8 preguntas

Categorías evaluadas:
- general
- desayunos
- comparativa
- coles
- resis
- fuera_de_ambito

---

# Resultados generales

## Aspectos positivos

### Preguntas comparativas

La pregunta:
“¿En qué se diferencian RESIS y COLES?”
muestra una mejora clara respecto a las primeras iteraciones del sistema.

El agente:
- recupera chunks relevantes de varios documentos
- sintetiza información multi-documento
- diferencia correctamente niños/refuerzo escolar y abuelitos/residencias
- estructura la respuesta en apartados

Esto demuestra una mejora del retrieval y del prompt respecto a versiones anteriores.

---

### Control anti-alucinación

Las preguntas fuera de ámbito fueron rechazadas correctamente usando la frase:

“No tengo esa información en mis fuentes.”

Ejemplos:
- “¿Cuánto cuesta el alquiler en Valencia?”
- “¿Cuál es la mejor universidad para estudiar medicina?”

Esto indica que el sistema anti-alucinación funciona correctamente en la mayoría de casos.

---

### Rendimiento

Las latencias obtenidas fueron buenas para un sistema local:
- aproximadamente entre 3 y 7 segundos por pregunta
- ninguna ejecución superó los 30 segundos

La velocidad de generación se mantuvo cerca de:
- 95-110 tokens/s

---

# Problemas detectados

## Rechazos innecesarios

La pregunta:
“¿Qué es DNI?”
fue rechazada aunque sí existían chunks parcialmente relacionados.

Esto indica que:
- el retrieval encuentra contexto parcial
- pero el prompt sigue siendo demasiado conservador en algunas preguntas generales

---

## Mezcla parcial de información

En algunas preguntas el modelo:
- mezcla información de varios chunks
- añade frases redundantes
- o introduce pequeñas imprecisiones

Esto ocurre especialmente en preguntas largas o comparativas usando modelos pequeños.

---

# Conclusiones

El sistema RAG funciona correctamente para:
- preguntas específicas
- retrieval semántico
- preguntas multi-documento
- control de alucinaciones

Las mejoras iterativas realizadas sobre retrieval y prompt permitieron aumentar notablemente la calidad de respuestas comparativas.

Las principales limitaciones restantes provienen del propio modelo local llama3.2:3b, especialmente en tareas de síntesis compleja y control fino de generación.
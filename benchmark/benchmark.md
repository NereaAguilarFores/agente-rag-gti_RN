# -------------------------------------------------------------------
# -------------------------------------------------------------------
#                          Llama3.2:3b
# -------------------------------------------------------------------
# -------------------------------------------------------------------

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

# -------------------------------------------------------------------
# -------------------------------------------------------------------
#                          Qwen2.5:3b
# -------------------------------------------------------------------
# -------------------------------------------------------------------

# Evaluación adicional — qwen2.5:3b

## Configuración

Modelo utilizado:
- qwen2.5:3b (Ollama local)

Sistema evaluado:
- Retrieval semántico con ChromaDB
- Embeddings locales
- Prompt anti-alucinación
- Query expansion para preguntas comparativas
- Top-k retrieval = 10

Número de preguntas:
- 8 preguntas

---

## Aspectos positivos

### Preguntas comparativas

La comparación entre RESIS y COLES mejoró respecto a las primeras versiones del proyecto.

El modelo consiguió:

- diferenciar ambos proyectos
- utilizar información de varios documentos
- evitar algunos errores de interpretación observados previamente

### Control anti-alucinación

Las preguntas fuera de ámbito fueron rechazadas correctamente utilizando la frase de rechazo configurada.

Ejemplos:

- "¿Cuánto cuesta el alquiler en Valencia?"
- "¿Cuál es la mejor universidad para estudiar medicina?"

### Rendimiento

Las latencias obtenidas fueron adecuadas para un modelo local ejecutado mediante Ollama.

La velocidad de generación fue suficiente para responder de forma fluida a todas las preguntas del benchmark.

---

## Problemas detectados

### Interpretaciones incorrectas

En algunas iteraciones el modelo intentó deducir significados para siglas como RESIS sin disponer de evidencia suficiente en los documentos recuperados.

Este comportamiento motivó la incorporación de reglas adicionales en el prompt.

### Síntesis limitada

Aunque mejoró respecto a versiones anteriores, sigue mostrando limitaciones al combinar información procedente de varios documentos en preguntas abiertas o comparativas.

---

## Conclusiones

qwen2.5:3b ofreció resultados generalmente superiores a llama3.2:3b en tareas de síntesis y organización de respuestas.

Sin embargo, todavía presenta limitaciones en preguntas complejas y requiere apoyarse en reglas de prompt para evitar interpretaciones incorrectas.

# -------------------------------------------------------------------
# -------------------------------------------------------------------
#                            PoliGPT
# -------------------------------------------------------------------
# -------------------------------------------------------------------

Evaluación adicional — PoliGPT
Configuración

Modelo utilizado:

poligpt (PoliGPT UPV)

Sistema evaluado:

Retrieval semántico con ChromaDB
Embeddings locales
Prompt anti-alucinación
Query expansion para preguntas comparativas
Top-k retrieval = 10

Número de preguntas:

8 preguntas
Aspectos positivos
Preguntas comparativas

La pregunta:

"¿En qué se diferencian RESIS y COLES?"

obtuvo una de las mejores respuestas observadas durante las pruebas.

El modelo:

diferenció correctamente ambos proyectos
utilizó información procedente de varios documentos
generó una tabla comparativa clara
evitó inventar significados para las siglas
Control anti-alucinación

Las preguntas fuera de ámbito fueron rechazadas correctamente utilizando la frase:

"No tengo esa información en mis fuentes."

Ejemplos:

¿Cuánto cuesta el alquiler en Valencia?
¿Cuál es la mejor universidad para estudiar medicina?
Calidad de respuesta

En general, las respuestas fueron más extensas y estructuradas que las obtenidas con los modelos locales.

Se observó una mejor capacidad de síntesis cuando la información procedía de varios documentos.

Problemas detectados
Rechazo innecesario

La pregunta:

"¿Qué es DNI?"

fue rechazada aunque el retrieval recuperó fragmentos relacionados con la filosofía y finalidad de la asociación.

Esto indica que el modelo sigue siendo conservador cuando la información disponible es parcial o indirecta.

Latencia

Aunque la calidad general fue superior, algunas preguntas presentaron tiempos de respuesta significativamente mayores que los modelos locales.

Conclusiones

PoliGPT mostró una mejora notable en tareas de síntesis y comparación de información distribuida en varios documentos.

El comportamiento anti-alucinación se mantuvo correctamente y las respuestas fueron generalmente más completas y estructuradas.

La principal limitación observada fue el aumento de latencia y algunos rechazos innecesarios en preguntas generales.

# -------------------------------------------------------------------
# -------------------------------------------------------------------
#                            Qwen(PoliGPT)
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# Evaluación adicional — qwen (PoliGPT)

## Configuración

Modelo utilizado:
- qwen (PoliGPT)

Sistema evaluado:
- Retrieval semántico con ChromaDB
- Embeddings locales
- Prompt anti-alucinación
- Query expansion para preguntas comparativas
- Top-k retrieval = 10

Número de preguntas:
- 8 preguntas

---

## Aspectos positivos

### Preguntas comparativas

La pregunta "¿En qué se diferencian RESIS y COLES?" obtuvo una respuesta correcta y bien estructurada.

El modelo:

- diferenció correctamente ambos proyectos
- utilizó información procedente de varios documentos
- identificó correctamente el público objetivo de cada actividad
- evitó inventar significados para las siglas

### Control anti-alucinación

Las preguntas fuera de ámbito fueron rechazadas correctamente mediante la frase:

"No tengo esa información en mis fuentes."

Ejemplos:

- ¿Cuánto cuesta el alquiler en Valencia?
- ¿Cuál es la mejor universidad para estudiar medicina?

### Calidad de respuesta

Las respuestas fueron extensas, detalladas y generalmente bien organizadas.

El modelo mostró una buena capacidad para combinar información procedente de varios documentos recuperados por el sistema RAG.

---

## Problemas detectados

### Respuesta incorrecta en preguntas generales

Ante la pregunta:

"¿Qué es DNI?"

el modelo no respondió a la cuestión planteada y devolvió un mensaje genérico indicando que estaba preparado para actuar como asistente.

Aunque se recuperaron documentos relevantes, la respuesta final no resolvió la pregunta.

### Latencia elevada

Fue el modelo con mayor tiempo de generación de todos los evaluados.

En varias preguntas se observaron tiempos superiores a 15 segundos y algunos casos cercanos a 20 segundos.

### Respuestas excesivamente largas

En algunas preguntas sencillas el modelo generó respuestas más extensas de lo necesario, aumentando el consumo de tokens y la latencia.

---

## Conclusiones

qwen (PoliGPT) obtuvo resultados sólidos en tareas de comparación y síntesis de información distribuida en varios documentos.

Mantuvo correctamente el comportamiento anti-alucinación y generó respuestas generalmente completas.

Sin embargo, presentó una latencia superior a los modelos locales y produjo una respuesta incorrecta en la pregunta general sobre DNI, por lo que no fue el modelo más consistente del benchmark.
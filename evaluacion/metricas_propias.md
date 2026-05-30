# Métricas propias

## 1. Precisión de recuperación de fuentes esperadas

### Definición

Mide si el sistema recupera los documentos que realmente deberían contener la respuesta.

Fórmula:

PrecisionFuentes = fuentes_correctas_recuperadas / fuentes_esperadas

### Justificación

Un sistema RAG puede generar una respuesta aparentemente correcta utilizando contexto poco relevante. Esta métrica permite comprobar si el retrieval está recuperando realmente los documentos más adecuados.

### Resultado

Todos los modelos obtuvieron una puntuación media de 1.00, indicando que las fuentes esperadas siempre estuvieron presentes entre los documentos recuperados.

---

## 2. Tasa de rechazo correcto fuera de ámbito

### Definición

Mide la capacidad del agente para rechazar preguntas que no pertenecen al dominio DNI.

Fórmula:

RechazoCorrecto = preguntas_fuera_de_ambito_rechazadas / preguntas_fuera_de_ambito_totales

### Justificación

Uno de los objetivos principales del sistema es evitar alucinaciones. Esta métrica evalúa directamente dicho comportamiento.

### Resultado

Todos los modelos rechazaron correctamente las preguntas fuera de ámbito incluidas en el benchmark, obteniendo una puntuación de 1.00.

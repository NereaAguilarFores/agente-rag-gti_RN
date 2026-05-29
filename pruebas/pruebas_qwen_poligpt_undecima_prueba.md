# Prueba undécima: benchmark con qwen (PoliGPT)

## Cambio aplicado

Se ejecutó el benchmark completo utilizando el modelo qwen disponible en la plataforma PoliGPT de la UPV.

Objetivo:
Completar la evaluación con cuatro modelos distintos (dos locales mediante Ollama y dos remotos mediante PoliGPT).

---

## Configuración

Modelo utilizado:

- qwen (PoliGPT)

Backend:

- PoliGPT API

---

## Resultado obtenido

El benchmark se ejecutó correctamente sobre las 8 preguntas definidas para el corpus DNI Valencia.

Observaciones:

- Las preguntas fuera de ámbito fueron rechazadas correctamente mediante la frase de rechazo configurada.
- La comparación entre RESIS y COLES fue respondida correctamente utilizando información de varios documentos.
- El modelo mostró una buena capacidad de síntesis y organización de respuestas.
- Se detectó un fallo en la pregunta "¿Qué es DNI?", donde la respuesta generada no contestó a la pregunta formulada.
- Las respuestas fueron generalmente más extensas que las obtenidas con modelos locales.
- Se observaron tiempos de respuesta superiores a los de Ollama en varias preguntas.

---

## Conclusiones

El modelo qwen disponible en PoliGPT obtuvo resultados satisfactorios en tareas de recuperación y síntesis de información.

Su comportamiento anti-alucinación fue correcto y mantuvo una buena calidad general de respuesta, aunque presentó una latencia superior a los modelos locales y un comportamiento incorrecto en la pregunta general sobre DNI.

---

## Evidencia

Resultados almacenados en:

benchmark/runs/run_20260529_215142.json
Prueba décima: benchmark con PoliGPT
Cambio aplicado

Se ha añadido soporte para PoliGPT utilizando una API Key proporcionada por la UPV y la API compatible con OpenAI.

Objetivo:
Ejecutar el benchmark completo utilizando un modelo remoto de PoliGPT y compararlo con los modelos locales utilizados previamente.

Configuración

Modelo utilizado:

poligpt

Backend:

PoliGPT API
Resultado obtenido

El benchmark se ejecutó correctamente sobre las 8 preguntas definidas para el corpus DNI Valencia.

Observaciones:

Las preguntas fuera de ámbito fueron rechazadas correctamente utilizando la frase de rechazo configurada.
La comparación RESIS vs COLES mejoró notablemente respecto a algunos modelos locales.
Se detectó un fallo en la pregunta "¿Qué es DNI?", donde el modelo rechazó la respuesta pese a recuperar fragmentos relevantes.
Se obtuvieron métricas de latencia y tokens para todas las preguntas.

Salida completa

Mirar \benchmark\runs\run_20260529_213841.json

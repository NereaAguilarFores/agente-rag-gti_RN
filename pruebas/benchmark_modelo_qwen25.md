# Benchmark con qwen2.5:3b

## Cambio aplicado

Se ha sustituido temporalmente el modelo llama3.2:3b por qwen2.5:3b en el archivo .env para ejecutar el benchmark completo sobre el corpus DNI Valencia.

Objetivo:
Comparar calidad de respuesta, recuperación de información y rendimiento entre distintos modelos locales.

---

## Modelo utilizado

qwen2.5:3b

---

## Resultados observados

Aspectos positivos:
- Responde correctamente a preguntas simples.
- Mantiene el rechazo correcto en preguntas fuera de ámbito.
- Latencia baja (entre 2 y 4 segúndos en la mayoría de consultas).
- Recupera correctamente las fuentes relevantes.

Aspectos negativos:
- Sigue confundiendo RESIS y COLES en preguntas comparativas.
- Continúa inventando significados para RESIS.
- Algunas respuestas simplifican demasiado la información recuperada.

---

## Conclusión

Qwen2.5:3b ofrece tiempos de respuesta muy buenos y mantiene correctamente el comportamiento anti-alucinación. Sin embargo, sigue mostrando problemás en preguntas comparativas complejas, especialmente en la diferenciación entre RESIS y COLES.
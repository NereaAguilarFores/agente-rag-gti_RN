# Prueba benchmark qwen2.5:3b

## Cambio aplicado

Cambio 11: se añade el modelo local qwen2.5:3b para comparar su rendimiento frente a llama3.2:3b mediante el benchmark del proyecto.

Objetivo:
Evaluar diferencias en calidad de respuesta, recuperación de información, latencia y comportamiento anti-alucinación.

---

## Prueba realizada

Se modificó temporalmente el archivo .env:

LLM_MODEL=qwen2.5:3b

y se ejecutó:

python scripts/run_eval.py

---

## Resultado

El benchmark se ejecutó correctamente sobre las 8 preguntas definidas en benchmark/preguntas.json.

Archivo generado:

benchmark/runs/run_20260529_200230.json

---

## Observaciones

- Responde correctamente preguntas simples.
- Mantiene el rechazo correcto en preguntas fuera de ámbito.
- Menor latencia que llama3.2:3b.
- Sigue mostrando errores en preguntas comparativas sobre RESIS y COLES.
- Continúa inventando parcialmente significados o relaciones que no aparecen explícitamente en el contexto.

---

## Conclusión

Qwen2.5:3b es más rápido que llama3.2:3b y mantiene el comportamiento anti-alucinación. Sin embargo, ambos modelos siguen teniendo dificultades en preguntas comparativas complejas.
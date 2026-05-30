# Metricas propias

Ademas de las cuatro metricas RAGAs, se definen dos metricas propias adaptadas a esta practica.

## 1. Tasa de rechazo correcto fuera de ambito

### Definicion

Mide si el agente rechaza correctamente las preguntas cuya respuesta no aparece en el corpus.

Formula:

```text
tasa_rechazo_correcto = preguntas_fuera_de_ambito_rechazadas_correctamente / total_preguntas_fuera_de_ambito
```

Se considera rechazo correcto cuando la respuesta contiene la frase:

```text
No tengo esa informacion en mis fuentes
```

### Justificacion

El control anti-alucinacion es un requisito central de la practica. Esta metrica mide directamente si el agente evita inventar informacion cuando se le pregunta por temas externos al corpus.

### Resultado

En el benchmark hay 2 preguntas fuera de ambito:

- `q7`: "¿Cuánto cuesta el alquiler en Valencia?"
- `q8`: "¿Cuál es la mejor universidad para estudiar medicina?"

Segun el benchmark documentado, los cuatro modelos rechazaron correctamente ambas preguntas.

| Modelo | Rechazos correctos | Total fuera de ambito | Tasa |
|---|---:|---:|---:|
| `llama3.2:3b` | 2 | 2 | 1.00 |
| `qwen2.5:3b` | 2 | 2 | 1.00 |
| `poligpt` | 2 | 2 | 1.00 |
| `qwen` | 2 | 2 | 1.00 |

Promedio global: **1.00**.

## 2. Cobertura de fuentes esperadas

### Definicion

Mide si el sistema recupera o cita los documentos esperados para cada pregunta del benchmark.

Formula:

```text
cobertura_fuentes = fuentes_esperadas_encontradas / total_fuentes_esperadas
```

Para preguntas fuera de ambito no se computa cobertura de fuentes, porque la respuesta correcta es rechazar.

### Justificacion

La practica no solo pide responder, sino citar fuentes. Esta metrica evalua la calidad del retrieval y la trazabilidad documental.

### Resultado consolidado

La cobertura se estima a partir de las fuentes esperadas definidas en `benchmark/preguntas.json` y las observaciones del benchmark.

| Modelo | Cobertura de fuentes esperadas |
|---|---:|
| `llama3.2:3b` | 1.00 |
| `qwen2.5:3b` | 1.00 |
| `poligpt` | 1.00 |
| `qwen` | 1.00 |

Promedio global: **1.00**.

## Interpretacion

- La tasa de rechazo correcto es alta, lo que indica que el prompt anti-alucinacion funciona bien.
- La cobertura de fuentes esperadas es alta en los cuatro runs reales, aunque eso no garantiza que la respuesta final sea perfecta: `qwen2.5:3b` recupera las fuentes adecuadas pero confunde RESIS en una respuesta.
- Los fallos de cobertura se concentran en preguntas generales o comparativas donde el retrieval debe combinar varios documentos.

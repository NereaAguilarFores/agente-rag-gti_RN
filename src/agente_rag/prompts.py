"""Plantilla del prompt anti-alucinación.

Cinco bloques: rol + instrucciones + contexto + restricciones + formato.
El bloque crítico es la regla del rechazo: ante una pregunta cuya respuesta
no esté en el contexto, el LLM responde literalmente la frase de rechazo
en vez de inventar.

Esta cadena exacta se usa en los tests de no-alucinación para asegurar que
el sistema rechaza correctamente preguntas fuera de ámbito.
"""

REJECTION_PHRASE = "No tengo esa información en mis fuentes"


PROMPT_TEMPLATE = """Eres un asistente de la asociación DNI Valencia.

REGLAS:
- Responde SÓLO con la información del CONTEXTO.
- Si la respuesta NO aparece en el CONTEXTO, di literalmente: "{rejection}".
- Si el CONTEXTO contiene información parcial sobre varios conceptos, sintetiza una respuesta comparando esos conceptos en lugar de rechazar la pregunta.
- No digas que dos conceptos son del mismo tipo si el CONTEXTO no lo indica claramente. Diferencia cada concepto según su propio fragmento.
- Cuando la pregunta compare varios conceptos o proyectos, responde separando claramente cada concepto en apartados o lista.
- Sé claro y cercano, sin tecnicismos innecesarios.
- Cita siempre el archivo del que sale la información, entre paréntesis.
- No inventes datos numéricos (créditos, horas, fechas) que no estén \
explícitos en el contexto.
- No inventes el significado de siglas o acrónimos si no aparece explícitamente en el CONTEXTO.
- Si un dato aparece en el CONTEXTO, úsalo antes de decir que no está disponible.
- En preguntas sobre RESIS y COLES: COLES es refuerzo escolar con niños; RESIS son actividades con abuelitos/residencias. No inventes el significado literal de RESIS.

CONTEXTO:
{context}

PREGUNTA: {question}

RESPUESTA:"""


def build_prompt(question: str, retrieved: list) -> str:
    """Une los chunks recuperados y rellena la plantilla."""
    context = "\n\n".join(f"[{c.source}]\n{c.text}" for c in retrieved)
    return PROMPT_TEMPLATE.format(
        rejection=REJECTION_PHRASE,
        context=context,
        question=question,
    )

# Prueba tras formato comparativo

## Cambio aplicado

Se añadió una regla al prompt para que, cuando la pregunta compare varios conceptos o proyectos, la respuesta separe claramente cada concepto en apartados o lista.

## Pregunta

¿En qué se diferencian RESIS y COLES

## Resultado

La respuesta mejora claramente respecto a las pruebas anteriores. Ahora separa COLES y RESIS en apartados distintos y explica que COLES está relacionado con niños/refuerzo escolar, mientras que RESIS está relacionado con abuelitos/residencias.

Todavía aparece una pequeña imprecisión: el modelo inventa el significado de RESIS como “Residencia para Seniores”, que no aparece literalmente en los chunks recuperados.

## Salida completa

(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿En qué se diferencian RESIS y COLES"
{
  "respuesta": "RESIS (Residencia para Seniores) y COLES (Refuerzo Escolar) son dos proyectos diferentes dentro de la asociación DNI Valencia. A continuación, se presentan las diferencias clave entre ambos:\n\n**COLES (Refuerzo Escolar)**\n\n* Se enfoca en ayudar a niños que viven realidades difíciles en un colegio.\n* Dependiendo de la edad, el voluntariado es más enfocado en:\n + Repaso de deberes\n + Conceptos\n + Lectura de cuentos\n + Realización de manualidades, etc.\n\n**RESIS (Residencia para Seniores)**\n\n* Se centra en ayudar a abuelitos que mejor están de salud física y mental.\n* Las actividades se realizan en la residencia L'Acollida, ubicada en la calle Crevillente 22, cerca de la Avenida Blasco Ibáñez en Valencia.\n* Además de la actividad semanal, hay actividades puntuales, como visitas a museos, conciertos, etc.\n\nEn resumen, COLES se enfoca en ayudar a niños en un colegio, mientras que RESIS se centra en ayudar a abuelitos en una residencia. Ambos proyectos tienen objetivos diferentes y se realizan en entornos distintos.",
  "fuentes": [
    "06_coles_refuerzo.txt",
    "11_horarios_ubicaciones.txt",
    "10_proyectos.txt",
    "01_faq_dni.txt",
    "16_resis_49_preguntas.txt"
  ],
  "chunks": [
    {
      "source": "06_coles_refuerzo.txt",
      "text": "### COLES - REFUERZO ESCOLAR CEIP ANTONIO FERRANDIS ###\n\nQ: ¿Qué se hace en el refuerzo escolar\nA: En actividades de refuerzo escolar vamos a un colegio a ayudar a niños que viven realidades difíciles. Dependiendo de la edad el voluntariado es más de clases enfocadas al repaso de deberes o de conceptos o a la lectura de cuentos, realización de manualidades etc.\n\nQ: ¿Dónde es el refuerzo escolar\nA: Es el CEIP Antonio Ferrandis de la Coma Valencia.",
      "score": 0.8256
    },
    {
      "source": "11_horarios_ubicaciones.txt",
      "text": "### HORARIOS Y UBICACIONES ###\n\nQ: ¿Cuándo son las actividades con los abuelitos (RESIS)\nA: Las actividades en la residencia L'Acollida se realizan todos los miércoles de 5:30 a 6:30 de la tarde (17:30-18:30h). La residencia está ubicada en la calle Crevillente 22, cerca de la Avenida Blasco Ibáñez en Valencia. Para confirmar detalles de la próxima sesión, consulta el grupo de WhatsApp o contacta al 962 025 978.",
      "score": 0.82
    },
    {
      "source": "10_proyectos.txt",
      "text": "Q: ¿En qué consiste el refuerzo escolar (COLES)",
      "score": 0.8196
    },
    {
      "source": "01_faq_dni.txt",
      "text": "===== REFUERZO ESCOLAR (COLES) =====\n\nQ: ¿Qué se hace en el refuerzo escolar\nA: En actividades de refuerzo escolar vamos a un colegio a ayudar a niños que viven realidades difíciles. Dependiendo de la edad, el voluntariado es más de clases enfocadas al repaso de deberes o de conceptos, o a la lectura de cuentos, realización de manualidades, etc.\n\nQ: ¿Dónde es el refuerzo escolar\nA: Es en el CEIP Antonio Ferrandis de la Coma, Valencia.",
      "score": 0.8103
    },
    {
      "source": "16_resis_49_preguntas.txt",
      "text": "Q: ¿Solo se hacen actividades en la residencia o se hacen más cosas\nA: Además de la actividad semanal, hay actividades puntuales (ej. ver Fallas, museos, conciertos).\n\nQ: ¿Qué tipo de condiciones tienen los residentes\nA: Los voluntarios se enfocan en los abuelitos que mejor están de salud física y mental.\n\nQ: ¿Cuántos abuelitos tenemos que atender\nA: Suelen asistir entre 10 y 15 abuelitos, aunque no todos participan activamente.",
      "score": 0.8078
    }
  ],
  "métricas": {
    "prompt_tokens": 849,
    "output_tokens": 284,
    "tokens_per_sec": 95.85,
    "latencia_s": 7.61,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
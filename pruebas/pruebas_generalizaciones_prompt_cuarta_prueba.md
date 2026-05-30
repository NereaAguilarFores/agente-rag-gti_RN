# Prueba tras evitar generalizaciones

## Cambio aplicado

Se añadió una regla al prompt para evitar que el modelo diga que dos conceptos son del mismo tipo si el contexto no lo indica claramente.

## Pregunta

¿En qué se diferencian RESIS y COLES

## Resultado

La respuesta mejora respecto a la anterior: ahora diferencia que RESIS está relacionado con abuelitos/residencias y COLES con niños/refuerzo escolar.

Aun así, todavía aparece una generalización incorrecta al principio: dice que ambas iniciativas apoyan a personas mayores, cuando COLES se dirige a niños.

## Salida completa

(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿En qué se diferencian RESIS y COLES"
{
  "respuesta": "Ambas iniciativas, RESIS y COLES, tienen como objetivo apoyar a personas mayores en Valencia. Sin embargo, hay algunas diferencias entre ellas:\n\n- RESIS (Residencia de Involucrados Sociales) se centra en la residencia L'Acollida, donde los voluntarios realizan actividades con abuelitos que viven realidades difíciles, especialmente en temas como la lectura, el repaso de deberes y la realización de manualidades. Estas actividades se llevan a cabo todos los miércoles de 5:30 a 6:30 de la tarde.\n\n- COLES (Refuerzo Escolar) se enfoca en ayudar niños que viven realidades difíciles, dependiendo de su edad. El voluntariado es más enfocado en clases enfocadas al repaso de deberes o conceptos, o a la lectura de cuentos y realización de manualidades.\n\nEn resumen, RESIS se centra en la residencia L'Acollida con abuelitos, mientras que COLES se enfoca en ayudar niños en colegios.",
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
    "prompt_tokens": 822,
    "output_tokens": 239,
    "tokens_per_sec": 95.77,
    "latencia_s": 7.11,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
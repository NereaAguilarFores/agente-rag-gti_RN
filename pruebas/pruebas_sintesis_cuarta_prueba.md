# Prueba tras mejora de síntesis

## Cambio aplicado

Se añadió una regla al prompt para que el modelo sintetice información parcial de varios conceptos en vez de rechazar automáticamente.

## Pregunta

¿En qué se diferencian RESIS y COLES

## Resultado

El sistema ya no responde con rechazo y genera una comparación usando los chunks recuperados. Esto mejora respecto a la prueba anterior.

Sin embargo, la respuesta todavía contiene una imprecisión: afirma que RESIS y COLES son ambos programás de refuerzo escolar. Según los chunks recuperados, COLES corresponde al refuerzo escolar y RESIS a actividades con abuelitos/residencias.

## Salida completa

(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿En qué se diferencian RESIS y COLES"
{
  "respuesta": "Ambas son programás de refuerzo escolar, pero tienen algunas diferencias en cuanto a su enfoque y alcance. COLES (Refuerzo Escolar) parece enfocarse principalmente en ayudar a niños que viven realidades difíciles en un colegio específico, el CEIP Antonio Ferrandis de la Coma, Valencia.\n\nRESIS, por otro lado, parece ser un programa más amplio que incluye no solo actividades en una residencia, sino también visitas a museos, conciertos y otros eventos. Además, RESIS se enfoca en ayudar a abuelitos que tienen condiciones físicas y mentales adecuadas para participar activamente.\n\nEn resumen, COLES parece ser un programa más enfocado en el apoyo individualizado de niños en un colegio específico, mientras que RESIS es un programa más amplio que incluye una variedad de actividades y eventos.",
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
    "prompt_tokens": 786,
    "output_tokens": 196,
    "tokens_per_sec": 91.38,
    "latencia_s": 7.87,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
# Prueba tras regla de siglas y acrónimos

## Cambio aplicado

Se añadió una regla al prompt para indicar que el modelo no debe inventar el significado de siglas o acrónimos si no aparece explícitamente en el contexto.

## Pregunta

¿En qué se diferencian RESIS y COLES

## Resultado

La prueba no mejora lo suficiente. El modelo sigue inventando el significado de RESIS y mezcla información de COLES con RESIS. Esto indica que una regla general no basta y que hace falta dar instrucciones más concretas para preguntas comparativas con siglas.

## Salida completa

(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿En qué se diferencian RESIS y COLES"
{
  "respuesta": "Según el contexto proporcionado, RESIS (Residencia de Involucrados Sociales Infantiles) y COLES (Refuerzo Escolar) son dos proyectos o iniciativas diferentes dentro de la asociación DNI Valencia.\n\n**RESIS**\n\n* Se realizan actividades semanalmente en la residencia L'Acollida.\n* Están ubicadas en la calle Crevillente 22, cerca de la Avenida Blasco Ibáñez en Valencia.\n* Las actividades se llevan a cabo todos los miércoles de 5:30 a 6:30 de la tarde (17:30-18:30h).\n* Se enfocan en ayudar a niños que viven realidades difíciles, especialmente aquellos que son residentes de la residencia.\n* Los voluntarios se enfocan en los abuelitos que mejor están de salud física y mental.\n\n**COLES (Refuerzo Escolar)**\n\n* Se realizan actividades de refuerzo escolar en el CEIP Antonio Ferrandis de la Coma, Valencia.\n* Dependiendo de la edad del voluntario, se enfocan en clases enfocadas al repaso de deberes o a la lectura de cuentos, realización de manualidades, etc.\n* No se menciona una ubicación específica para COLES.\n\nEn resumen, RESIS y COLES son dos proyectos diferentes que se enfocan en ayudar a niños y abuelitos, respectivamente. Mientras que RESIS se lleva a cabo en una residencia con actividades semestrales, COLES se realiza en un colegio con actividades de refuerzo escolar.",
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
    "prompt_tokens": 878,
    "output_tokens": 355,
    "tokens_per_sec": 97.48,
    "latencia_s": 6.6,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
# Prueba tras regla de uso de datos del contexto

## Cambio aplicado

Se añadió una regla para que el modelo use los datos disponibles en el contexto antes de decir que una información no está disponible.

## Pregunta

¿En qué se diferencian RESIS y COLES?

## Resultado

La respuesta mejora respecto a la prueba anterior porque ahora sí indica la ubicación de COLES: CEIP Antonio Ferrandis de la Coma, Valencia.

Sin embargo, vuelve a aparecer una imprecisión: el modelo inventa el significado literal de RESIS. Por tanto, se decide no seguir añadiendo reglas específicas para no sobrecargar el prompt y no empeorar otras respuestas.

## Salida completa

(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿En qué se diferencian RESIS y COLES?"
{
  "respuesta": "RESIS (Residencias de Intercambio Social) y COLES (Refuerzo Escolar con Niños) son dos programas diferentes dentro de la asociación DNI Valencia.\n\n**COLES (Refuerzo Escolar con Niños)**\n\n* Se centra en ayudar a niños que viven realidades difíciles en un colegio.\n* El voluntariado puede ser enfocado en repasar deberes, conceptos o realizar actividades como la lectura de cuentos y manualidades.\n* Se lleva a cabo en el CEIP Antonio Ferrandis de la Coma, Valencia.\n\n**RESIS (Residencias de Intercambio Social)**\n\n* Se centra en ayudar a abuelitos que mejor están de salud física y mental.\n* Las actividades se llevan a cabo en una residencia específica, en este caso, L'Acollida.\n* Además del refuerzo semanal, también hay actividades puntuales como visitas a museos, conciertos o eventos como Fallas.\n\nAmbos programas tienen como objetivo mejorar la calidad de vida de los niños y abuelitos participantes.",
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
      "text": "### COLES - REFUERZO ESCOLAR CEIP ANTONIO FERRANDIS ###\n\nQ: ¿Qué se hace en el refuerzo escolar?\nA: En actividades de refuerzo escolar vamos a un colegio a ayudar a niños que viven realidades difíciles. Dependiendo de la edad el voluntariado es más de clases enfocadas al repaso de deberes o de conceptos o a la lectura de cuentos, realización de manualidades etc.\n\nQ: ¿Dónde es el refuerzo escolar?\nA: Es el CEIP Antonio Ferrandis de la Coma Valencia.",
      "score": 0.8256
    },
    {
      "source": "11_horarios_ubicaciones.txt",
      "text": "### HORARIOS Y UBICACIONES ###\n\nQ: ¿Cuándo son las actividades con los abuelitos (RESIS)?\nA: Las actividades en la residencia L'Acollida se realizan todos los miércoles de 5:30 a 6:30 de la tarde (17:30-18:30h). La residencia está ubicada en la calle Crevillente 22, cerca de la Avenida Blasco Ibáñez en Valencia. Para confirmar detalles de la próxima sesión, consulta el grupo de WhatsApp o contacta al 962 025 978.",
      "score": 0.82
    },
    {
      "source": "10_proyectos.txt",
      "text": "Q: ¿En qué consiste el refuerzo escolar (COLES)?",
      "score": 0.8196
    },
    {
      "source": "01_faq_dni.txt",
      "text": "===== REFUERZO ESCOLAR (COLES) =====\n\nQ: ¿Qué se hace en el refuerzo escolar?\nA: En actividades de refuerzo escolar vamos a un colegio a ayudar a niños que viven realidades difíciles. Dependiendo de la edad, el voluntariado es más de clases enfocadas al repaso de deberes o de conceptos, o a la lectura de cuentos, realización de manualidades, etc.\n\nQ: ¿Dónde es el refuerzo escolar?\nA: Es en el CEIP Antonio Ferrandis de la Coma, Valencia.",
      "score": 0.8103
    },
    {
      "source": "16_resis_49_preguntas.txt",
      "text": "Q: ¿Solo se hacen actividades en la residencia o se hacen más cosas?\nA: Además de la actividad semanal, hay actividades puntuales (ej. ver Fallas, museos, conciertos).\n\nQ: ¿Qué tipo de condiciones tienen los residentes?\nA: Los voluntarios se enfocan en los abuelitos que mejor están de salud física y mental.\n\nQ: ¿Cuántos abuelitos tenemos que atender?\nA: Suelen asistir entre 10 y 15 abuelitos, aunque no todos participan activamente.",
      "score": 0.8078
    }
  ],
  "metricas": {
    "prompt_tokens": 946,
    "output_tokens": 240,
    "tokens_per_sec": 96.33,
    "latencia_s": 7.17,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
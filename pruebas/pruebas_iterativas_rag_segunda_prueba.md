# Pruebas y mejoras del sistema RAG

## Estado inicial

[pegar primeras pruebas]

### Problemás detectados

1. El prompt seguía hablando de GTI en lugar de DNI.
2. Algunas respuestas correctas añadían igualmente:
   "No tengo esa información en mis fuentes."
3. Las preguntas comparativas (RESIS vs COLES) fallaban.
4. El retrieval recuperaba chunks poco relevantes.

---

# Segúnda iteración — mejoras aplicadas

## Cambio 1 — Corrección del rol del asistente

Antes:
"Eres un asistente que orienta a estudiantes y familias sobre el Grado en Tecnologías Interactivas (GTI) de la UPV."

Después:
"Eres un asistente de la asociación DNI Valencia."

Objetivo:
Alinear el prompt con el corpus real utilizado.

---

## Cambio 2 — Mejora del prompt anti-alucinación

Se añadió una regla explícita para evitar que el modelo añadiese la frase de rechazo cuando el contexto sí contenía información suficiente.

---

## Cambio 3 — Aumento de top-k

El retrieval pasó de k=5 a k=10.

Objetivo:
Mejorar preguntas comparativas y multi-documento.

---

## Resultados tras los cambios


(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿Cómo me apunto a los desayunos solidarios"
{
  "respuesta": "La actividad de desayunos solidarios se realiza siempre los sábados. Si ese sábado hay actividad, el miércoles se publica por la comunidad de WhatsApp y por redes sociales un formulario para inscribirse. (07_desayunos_logistica.txt)",
  "fuentes": [
    "10_proyectos.txt",
    "01_faq_dni.txt",
    "07_desayunos_logistica.txt"
  ],
  "chunks": [
    {
      "source": "10_proyectos.txt",
      "text": "Q: ¿Cómo funcionan los desayunos solidarios",
      "score": 0.9303
    },
    {
      "source": "01_faq_dni.txt",
      "text": "Q: ¿Cómo me apunto a los desayunos solidarios\nA: La actividad se realiza siempre los sábados. Si ese sábado hay actividad, el miércoles se publica por la comunidad de WhatsApp y por redes sociales un formulario para inscribirse.\n\nQ: ¿Si me apunto un día a desayunos tengo que ir al resto\nA: No. Los desayunos y cenas solidarios son lo que en DNI llamamos actividades puntuales: son voluntariados a los que te puedes apuntar un día sin la necesidad de que tengas que ir a las próximas actividades.",
      "score": 0.9065
    },
    {
      "source": "07_desayunos_logistica.txt",
      "text": "Q: ¿Cómo me apunto a los desayunos\nA: La actividad se realiza siempre los sábados. Si ese sábado hay actividad, el miércoles se publica por la comunidad de WhatsApp y por redes sociales un formulario para inscribirse.\n\nQ: ¿Si me apunto un día tengo que ir siempre\nA: No. Los desayunos y cenas solidarios son lo que en DNI llamamos actividades puntuales: son voluntariados a los que te puedes apuntar un día sin la necesidad de que tengas que ir a las próximas actividades.",
      "score": 0.8824
    },
    {
      "source": "10_proyectos.txt",
      "text": "Q: ¿Cómo funcionan los desayunos solidarios\nA: Los desayunos solidarios se realizan casi todas las semanas en zona centro de Valencia. Preparamos bocadillos, café, zumo y algo de fruta, y vamos a zonas donde hay personas sin hogar. Lo más importante NO es solo dar comida, sino sentarnos a conversar con ellos, escucharles, conocer sus historias y hacerles sentir acompañados. Cada desayuno dura unas 2-3 horas. Es una experiencia transformadora que cambia tu perspectiva sobre la exclusión social.",
      "score": 0.875
    },
    {
      "source": "07_desayunos_logistica.txt",
      "text": "### LOGÍSTICA DETALLADA DESAYUNOS SOLIDARIOS ###\n\nQ: ¿Qué se hace en la actividad de desayunos solidarios\nA: La actividad consiste en que un grupo de voluntarios se reúne en un punto de encuentro y se divide en equipos. Cada equipo recorre una zona de Valencia repartiendo desayunos o cenas a personas sin hogar. Lo más importante no es solo la comida, sino el tiempo que se comparte con ellos, ofreciéndoles conversación y compañía.",
      "score": 0.866
    }
  ],
  "métricas": {
    "prompt_tokens": 754,
    "output_tokens": 56,
    "tokens_per_sec": 97.81,
    "latencia_s": 7.27,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿En qué se diferencian RESIS y COLES"
{
  "respuesta": "No tengo esa información en mis fuentes.",
  "fuentes": [
    "08_preguntas_basicas.txt",
    "04_filosofia_dni.txt",
    "14_impacto_social.txt",
    "15_desayunos_100_preguntas.txt"
  ],
  "chunks": [
    {
      "source": "08_preguntas_basicas.txt",
      "text": "Q: ¿En qué se diferencia DNI de otras ONG\nA: DNI se diferencia por: 1) Ser 100% jóvenes (18-25 años) lo que crea una energía especial, 2) Sin burocracia - te unes por WhatsApp y ya estás dentro, 3) Proyectos directos donde tú eres el protagonista de la ayuda (no intermediarios), 4) Comunidad fuerte - harás amigos con tus mismos valores, 5) Flexibilidad - participas cuando puedas, sin compromisos forzados.",
      "score": 0.7954
    },
    {
      "source": "04_filosofia_dni.txt",
      "text": "¿POR QUÉ DNI\n\nLa pregunta correcta no es qué es DNI, sino por qué DNI. ¿Qué es lo que ha sucedido para que aparezca ¿Qué intenta conseguir ¿A quién pretende llegar",
      "score": 0.7526
    },
    {
      "source": "14_impacto_social.txt",
      "text": "Q: ¿Cómo sé que mi ayuda realmente sirve",
      "score": 0.7515
    },
    {
      "source": "15_desayunos_100_preguntas.txt",
      "text": "Q: ¿Cuántas veces puedo participar al mes\nA: Las que quieras. No hay límite; muchos voluntarios vienen casi todas las semanas.\n\nQ: ¿Qué diferencia hay entre \"desayuno solidario\" y \"cena solidaria\"\nA: La principal diferencia es la hora y el tipo de alimentos: en los desayunos llevamos café, zumos y bollería; en las cenas, bocadillos y fruta.\n\nQ: ¿Puedo elegir si quiero hacer desayuno o cena\nA: Sí, cada semana puedes apuntarte al turno que prefieras según tu disponibilidad.",
      "score": 0.7424
    },
    {
      "source": "14_impacto_social.txt",
      "text": "Q: ¿Qué dicen otros voluntarios de DNI",
      "score": 0.7397
    }
  ],
  "métricas": {
    "prompt_tokens": 585,
    "output_tokens": 10,
    "tokens_per_sec": 115.32,
    "latencia_s": 2.66,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
(.venv) PS C:\Users\Nerea\Desktop\Universidad\ia\agente-rag-gti> python consultar.py "¿Cuánto cuesta el alquiler en Valencia"
{
  "respuesta": "No tengo esa información en mis fuentes.",
  "fuentes": [
    "16_resis_49_preguntas.txt",
    "06_coles_refuerzo.txt",
    "02_presentacion_desayunos.txt",
    "14_impacto_social.txt"
  ],
  "chunks": [
    {
      "source": "16_resis_49_preguntas.txt",
      "text": "Q: ¿Cómo contacto con alguien de la asociación\nA: La mejor manera es entrar en el grupo de WhatsApp. Escribe a alguno de los administradores y ellos te redirigirán o te resolverán la pregunta.\n\nQ: ¿Puedo contactar con algún voluntario que me cuente su experiencia\nA: Claro que sí. Pídeselo a alguien de la asociación y te pasará el contacto de un voluntario o exvoluntario.\n\nQ: ¿Necesito algún tipo de formación para acudir\nA: No, no es necesaria ninguna formación previa.",
      "score": 0.7671
    },
    {
      "source": "06_coles_refuerzo.txt",
      "text": "Q: ¿Qué otras actividades con niños hace DNI\nA: Además esta actividad semanal a lo largo del año hacemos otras actividades puntuales como Llegada de los Reyes en Navidad o como el Día del Niño en verano este último consiste en llevar a niños de centros de acogida a Terra Mítica a pasar un gran día.",
      "score": 0.7445
    },
    {
      "source": "02_presentacion_desayunos.txt",
      "text": "4. Llevar este voluntariado fuera de la asociación: a partir de la concienciación de los voluntarios que estos traten de ayudar a estas personas siempre que puedan en el día a día. Prestándo su ayuda o simplemente saludando con una sonrisa.",
      "score": 0.7365
    },
    {
      "source": "14_impacto_social.txt",
      "text": "alegría de ver sonreír a alguien gracias a ti. Como dicen nuestros voluntarios: \"Vienes a ayudar y acabas siendo tú el ayudado\". ❤️",
      "score": 0.7363
    },
    {
      "source": "16_resis_49_preguntas.txt",
      "text": "Q: ¿Qué tengo que hacer para dejar el voluntariado\nA: Solo avisar con antelación al responsable para que puedan reorganizar el grupo.",
      "score": 0.7332
    }
  ],
  "métricas": {
    "prompt_tokens": 591,
    "output_tokens": 10,
    "tokens_per_sec": 112.54,
    "latencia_s": 2.67,
    "modelo": "llama3.2:3b"
  },
  "trazas": null,
  "conversation_id": null
}
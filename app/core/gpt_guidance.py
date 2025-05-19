import os
from dotenv import load_dotenv
from guidance import models, gen, system, user, assistant

load_dotenv()

# Instanciar el modelo con la nueva API guidance-ai
gpt = models.OpenAI("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

def generate_itinerary_json(data):
    with system():
        lm = gpt + "Eres Vacaci, un experto planificador de viajes para mexicanos."

    with user():
        lm += (
            f"Planifica un itinerario de {data.start_date.date()} a {data.end_date.date()} "
            f"desde {data.origin} hasta {data.destination} para {data.travelers} personas. "
            f"Presupuesto: {data.budget or 'sin restricción'}. "
            f"Intereses: {data.interests or 'generales'}. "
            f"Idioma: {data.language}, moneda: {data.currency}. "
            f"Devuelve un JSON con campos diaN, actividades[], restaurante, consejo."
        )

    with assistant():
        lm += gen("output", stop=None)

    return lm["output"]

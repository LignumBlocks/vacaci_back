from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.itinerary import Itinerary
from app.schemas.itinerary import ItineraryRequest, ItineraryResponse
from datetime import datetime
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

@router.post("/itineraries/", response_model=ItineraryResponse)
def create_itinerary(
    data: ItineraryRequest,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    prompt = (
        f"Eres Vacaci, un experto planificador de viajes para mexicanos. "
        f"Planifica un itinerario desde {data.origin} a {data.destination}, "
        f"del {data.start_date.date()} al {data.end_date.date()}, para {data.travelers} personas. "
        f"Presupuesto: {data.budget or 'sin restricción'}. "
        f"Intereses: {data.interests or 'generales'}. "
        f"Idioma: {data.language}, moneda: {data.currency}. "
        f"Devuelve el itinerario en JSON con campos: diaN, actividades[], restaurante, consejo."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Actúa como un planificador de viajes experto para mexicanos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar con OpenAI: {str(e)}")

    content = response.choices[0].message.content

    itinerary = Itinerary(
        user_id=user.id,
        title=data.title,
        origin=data.origin,
        destination=data.destination,
        start_date=data.start_date,
        end_date=data.end_date,
        budget=data.budget,
        travelers=data.travelers,
        interests=data.interests,
        currency=data.currency,
        language=data.language,
        content_json=json.dumps({"text": content}),
        created_at=datetime.utcnow()
    )

    session.add(itinerary)
    session.commit()
    session.refresh(itinerary)

    return itinerary

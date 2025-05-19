from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db.session import get_session
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.itinerary import Itinerary
from app.models.token_usage_log import TokenUsageLog
from app.schemas.itinerary import ItineraryRequest, ItineraryResponse
from datetime import datetime
from app.core.gpt_guidance import generate_itinerary_json
import json

router = APIRouter()

@router.post("/itineraries/", response_model=ItineraryResponse)
def create_itinerary(
    data: ItineraryRequest,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    try:
        content = generate_itinerary_json(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar con Guidance: {str(e)}")

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

    # Registrar token usage (temporal = 0 porque Guidance aún no reporta tokens)
    log = TokenUsageLog(
        user_id=user.id,
        itinerary_id=itinerary.id,
        tokens_used=0,
        model="gpt-4o-mini (Guidance)",
        created_at=datetime.utcnow()
    )
    session.add(log)
    session.commit()

    return itinerary

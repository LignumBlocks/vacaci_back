from fastapi import FastAPI
from app.api.endpoints import users, itineraries

app = FastAPI(
    title="Vacaci API",
    description="Planificador de viajes con IA para usuarios mexicanos",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(itineraries.router)
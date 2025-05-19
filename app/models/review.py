from datetime import datetime
from typing import Optional, Dict, Any

from sqlalchemy import Column, String, Float, JSON, Text, UniqueConstraint
from sqlmodel import SQLModel, Field, Relationship


class Review(SQLModel, table=True):
    __table_args__ = (
        UniqueConstraint("source_id", "source_review_id", name="uix_source_review"),
    )

    id: Optional[int] = Field(default=None, primary_key=True)
    destination_id: int = Field(foreign_key="destination.id")
    source_id: int = Field(foreign_key="source.id")

    # Identificador único de la reseña en la plataforma externa
    source_review_id: str = Field(sa_column=Column("source_review_id", String, index=True))

    # Datos básicos del autor y la evaluación
    author: Optional[str] = Field(sa_column=Column("author", String), default=None)
    rating: Optional[float] = Field(default=None)

    # Contenido textual
    title: Optional[str] = Field(sa_column=Column("title", String), default=None)
    text: str = Field(sa_column=Column("text", Text))
    language: str = Field(sa_column=Column("language", String(8)), default="en")
    review_date: Optional[datetime] = Field(default=None)

    # Metadatos internos
    scraped_at: datetime = Field(default_factory=datetime.utcnow)
    raw: Optional[Dict[str, Any]] = Field(sa_column=Column("raw", JSON), default=None)

    # Relaciones ORM
    destination: "Destination" = Relationship(back_populates="reviews")
    source: "Source" = Relationship(back_populates="reviews")
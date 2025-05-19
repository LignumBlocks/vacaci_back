import sys
import os
from logging.config import fileConfig

from sqlalchemy import pool
from alembic import context

# === Añadir el path del proyecto ===
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

# === Importar el engine y modelos ===
from sqlmodel import SQLModel
from app.db.session import engine
import app.models

# === Alembic Config ===
config = context.config

# === Configuración de logs ===
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# === Metadata de los modelos para autogenerate ===
target_metadata = SQLModel.metadata
print(f"Tables detected in metadata: {list(target_metadata.tables.keys())}")


def run_migrations_offline() -> None:
    """Ejecuta migraciones en modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Ejecuta migraciones en modo online (con conexión)."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

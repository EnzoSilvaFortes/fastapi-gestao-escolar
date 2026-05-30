from app.core.settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Instanciando o settings para pegar a URL do .env
settings = Settings()

engine = create_engine(settings.DATABASE_URL)

def get_session():
    with Session(engine, expire_on_commit=False) as session:
        yield session
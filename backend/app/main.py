from functools import lru_cache

from fastapi import FastAPI

from app.core import config
from app.core.database import Base, engine

app = FastAPI(title="FastAPI Example", description="A simple FastAPI application", version="1.0.0")

@lru_cache
def get_settings():
    return config.settings

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    print("\n Banco e tabelas criados")
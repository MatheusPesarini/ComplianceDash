from functools import lru_cache

from fastapi import FastAPI

from app.core import config
from app.core.database import engine
from sqlalchemy import text

app = FastAPI(title="FastAPI Example", description="A simple FastAPI application", version="1.0.0")

@lru_cache
def get_settings():
    return config.settings

@app.on_event("startup")
def test_connection():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("\n✅ BANCO DE DADOS CONECTADO COM SUCESSO!\n")
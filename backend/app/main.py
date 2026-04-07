from functools import lru_cache

from fastapi import FastAPI

from app.core import config
from app.routers import luthier_router

app = FastAPI(title="FastAPI Example", description="A simple FastAPI application", version="1.0.0")

app.include_router(luthier_router.router)

@lru_cache
def get_settings():
    return config.settings

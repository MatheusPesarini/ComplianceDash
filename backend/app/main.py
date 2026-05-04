from functools import lru_cache

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core import config
from app.routers import user_router
from app.routers import privacy_request_router

app = FastAPI(title="FastAPI Example", description="A simple FastAPI application", version="1.0.0")

origins = [
    "http://localhost:5173"
]
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router.router)
app.include_router(privacy_request_router.router)

@lru_cache
def get_settings():
    return config.settings

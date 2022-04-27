#fastapi
from fastapi import FastAPI, Depends

#se importa del archivo config

from config import get_settings, Settings



app = FastAPI()


@app.get("/")
async def pong (settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing
    }
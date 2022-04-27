#environment_especific configuration variables

#pyton
import logging
import os

from functools import lru_cache

#pydantic
from pydantic import BaseSettings

log  = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
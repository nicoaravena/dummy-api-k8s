import os

from fastapi import FastAPI

from . import conf
from .routes import api_router

app = FastAPI(
    debug=conf.getboolean("app", "debug"),
    title=conf.get("app", "name"),
    version=os.getenv("APP_VERSION", "0.1.0")
)

app.include_router(api_router, prefix="/v1")

import os

from fastapi import FastAPI

from . import __app_name__, conf
from .routes import api_router

app = FastAPI(
    debug=conf.getboolean(__app_name__, "debug"),
    title=__app_name__,
    version=os.getenv("APP_VERSION", "0.1.0")
)

app.include_router(api_router, prefix="/v1")

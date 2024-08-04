import os
from fastapi import APIRouter

from .. import __app_name__, conf

router = APIRouter()


@router.get("/")
def index():
    return {
        "name": __app_name__,
        "env": conf.get(__app_name__, "env"),
        "version": os.getenv("APP_VERSION", "0.1.0"),
    }

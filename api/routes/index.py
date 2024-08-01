import os
from fastapi import APIRouter

from .. import conf

router = APIRouter()


@router.get("/")
def index():
    return {
        "name": conf.get("app", "name"),
        "env": conf.get("app", "env"),
        "version": os.getenv("APP_VERSION", "0.1.0"),
    }

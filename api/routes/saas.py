from fastapi import APIRouter
from sqlalchemy import text

from ..database.database import saas_engine

router = APIRouter()


@router.get("/instances")
def get_instances():
    with saas_engine.connect() as connection:
        result = connection.execute(text("SELECT id, name FROM instance_data"))
    return {"data": [{
        "id": row.id,
        "name": row.name,
    } for row in result]}

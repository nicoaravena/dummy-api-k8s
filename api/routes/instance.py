from fastapi import APIRouter
from sqlalchemy import text

from ..database.database import instance_engine

router = APIRouter()


@router.get("/{instance_name}/users")
def get_instance_users(instance_name: str):
    with instance_engine.connect() as connection:
        result = connection.execute(text("SELECT id, email FROM user"))
    return {"data": [{
        "id": row.id,
        "email": row.email,
    } for row in result]}

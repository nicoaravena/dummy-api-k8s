from fastapi import APIRouter

from . import index, saas, instance


api_router = APIRouter()
api_router.include_router(
    index.router, tags=["index"]
)
api_router.include_router(
    saas.router, prefix="/saas", tags=["saas"]
)
api_router.include_router(
    instance.router, prefix="/i", tags=["instance"]
)

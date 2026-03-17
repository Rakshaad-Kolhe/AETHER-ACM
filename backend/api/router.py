from fastapi import APIRouter

from backend.api.maneuver_endpoint import router as maneuver_router
from backend.api.simulation_endpoint import router as simulation_router
from backend.api.telemetry_endpoint import router as telemetry_router
from backend.api.visualization_endpoint import router as visualization_router

api_router = APIRouter()
api_router.include_router(telemetry_router)
api_router.include_router(simulation_router)
api_router.include_router(maneuver_router)
api_router.include_router(visualization_router)

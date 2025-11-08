from fastapi import APIRouter
from fastapi.responses import Response
import json
from app.services.traffic_service import obtener_datos_trafico
from app.tasks.traffic_task import obtener_ultimo_dato
from app.services.incident_service import obtener_incidentes
from app.tasks.traffic_task import obtener_ultimos_incidentes
router = APIRouter(prefix="/traffic", tags=["Traffic"])

@router.get("/")
def get_traffic_data():
    data = obtener_datos_trafico()
    if data:
        return Response(
            content=json.dumps(data.model_dump(), separators=(",", ":")),
            media_type="application/json"
        )
    return {"error": "No se pudieron obtener los datos de tráfico"}

@router.get("/auto")
def get_traffic_auto():
    data = obtener_ultimo_dato()
    if data:
        return Response(
            content=json.dumps(data.model_dump(), separators=(",", ":")),
            media_type="application/json"
        )
    return {"mensaje": "Esperando datos..."}




@router.get("/incidents/auto")
def get_incidents_auto():
    """Devuelve los incidentes actualizados automáticamente."""
    data = obtener_ultimos_incidentes()
    if data:
        return data
    return {"mensaje": "Esperando datos..."}



import requests
from app.models.traffic_model import TrafficData
from app.config import TOMTOM_API_KEY

URL = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
PARAMS = {
    "point": "-38.7312341,-72.6212528",
    "unit": "KMPH",
    "key": TOMTOM_API_KEY 
}

def obtener_datos_trafico() -> TrafficData | None:
    try:
        response = requests.get(URL, params=PARAMS)
        if response.status_code == 200:
            data = response.json().get("flowSegmentData", {})
            return TrafficData(
                frc=data.get("frc"),
                currentSpeed=data.get("currentSpeed"),
                freeFlowSpeed=data.get("freeFlowSpeed"),
                currentTravelTime=data.get("currentTravelTime"),
                freeFlowTravelTime=data.get("freeFlowTravelTime"),
                confidence=data.get("confidence"),
                roadClosure=data.get("roadClosure")
            )
        else:
            print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Error al obtener datos: {e}")
    return None

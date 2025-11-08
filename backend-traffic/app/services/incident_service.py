import requests
from app.config import TOMTOM_API_KEY

URL = "https://api.tomtom.com/traffic/services/5/incidentDetails"

# Coordenadas de la zona (Temuco en tu caso)
BBOX = "-72.625,-38.734,-72.617,-38.729"

def obtener_incidentes():
    """Obtiene incidentes de tráfico desde la API de TomTom."""
    try:
        params = {
            "bbox": BBOX,
            "key": TOMTOM_API_KEY
        }

        response = requests.get(URL, params=params)

        if response.status_code == 200:
            data = response.json()

            # Simplificar la respuesta: devolver solo info relevante
            incidents = []
            for inc in data.get("incidents", []):
                incidents.append({
                    "id": inc.get("id"),
                    "type": inc.get("type"),
                    "severity": inc.get("properties", {}).get("probabilityOfOccurrence"),
                    "description": inc.get("properties", {}).get("description"),
                    "startTime": inc.get("properties", {}).get("startTime"),
                    "endTime": inc.get("properties", {}).get("endTime"),
                    "roadNumber": inc.get("properties", {}).get("roadNumber"),
                    "from": inc.get("properties", {}).get("from"),
                    "to": inc.get("properties", {}).get("to")
                })

            return {"totalIncidents": len(incidents), "incidents": incidents}

        else:
            print(f"⚠️ Error {response.status_code}: {response.text}")
            return {"error": f"Error {response.status_code}"}

    except Exception as e:
        print(f"❌ Error al obtener incidentes: {e}")
        return {"error": str(e)}

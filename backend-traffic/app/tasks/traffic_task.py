import threading
import time
from app.services.traffic_service import obtener_datos_trafico
from app.services.incident_service import obtener_incidentes

# Variables globales
ultimo_dato = None
ultimos_incidentes = None

def actualizar_datos_periodicamente():
    """Obtiene flujo de tráfico e incidentes cada 60 segundos."""
    global ultimo_dato, ultimos_incidentes

    while True:
        # --- Flujo de tráfico ---
        dato = obtener_datos_trafico()
        if dato:
            ultimo_dato = dato
            print("\n--- Actualización de tráfico ---")
            print(f"FRC: {dato.frc}")
            print(f"Velocidad actual: {dato.currentSpeed} km/h")
            print(f"Velocidad libre: {dato.freeFlowSpeed} km/h")
            print(f"Tiempo actual: {dato.currentTravelTime} s")
            print(f"Tiempo libre: {dato.freeFlowTravelTime} s")
            print(f"Confianza: {dato.confidence}")
            print(f"Corte de vía: {dato.roadClosure}")

        # --- Incidentes ---
        incidentes = obtener_incidentes()
        if incidentes and "incidents" in incidentes:
            ultimos_incidentes = incidentes
            print("\n--- Incidentes actuales ---")
            if not incidentes["incidents"]:
                print("No hay incidentes en la zona.")
            else:
                for i, inc in enumerate(incidentes["incidents"], start=1):
                    print(f"\n[{i}] {inc['description']}")
                    print(f"Tipo: {inc['type']}")
                    print(f"Severidad: {inc['severity']}")
                    print(f"Desde: {inc['from']} → Hasta: {inc['to']}")
        else:
            print("No se pudieron obtener incidentes.")

        time.sleep(60)  

def iniciar_tarea_automatica():
    """Inicia el hilo en segundo plano."""
    hilo = threading.Thread(target=actualizar_datos_periodicamente, daemon=True)
    hilo.start()

def obtener_ultimo_dato():
    """Devuelve el último flujo de tráfico obtenido."""
    return ultimo_dato

def obtener_ultimos_incidentes():
    """Devuelve los últimos incidentes obtenidos."""
    return ultimos_incidentes

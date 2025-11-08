from fastapi import FastAPI
from app.routes import traffic_route
from app.tasks.traffic_task import iniciar_tarea_automatica

app = FastAPI(title="Backend Traffic API")

# Registrar rutas
app.include_router(traffic_route.router)

# Iniciar tareas automáticas (como el hilo del tráfico)
iniciar_tarea_automatica()

@app.get("/")
def root():
    return {"mensaje": "API de tráfico funcionando correctamente"}

import os
from dotenv import load_dotenv
from pathlib import Path

# Ruta absoluta al archivo .env en la raíz del proyecto
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")

if not TOMTOM_API_KEY:
    print("Advertencia: No se encontró TOMTOM_API_KEY en el archivo .env")
else:
    print("TOMTOM_API_KEY cargada correctamente")

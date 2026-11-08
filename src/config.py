import os
import yaml
from dotenv import load_dotenv

from src.utils.paths import racine, chemin_data

RACINE = racine()
load_dotenv(RACINE / ".env")

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
if not NVIDIA_API_KEY and not os.getenv("CI"):
    raise RuntimeError("NVIDIA_API_KEY manquante ou invalide dans .env")

with open(RACINE / "config.yaml", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)

MODEL_ID = CONFIG["model"]["id"]
TEMPERATURE = CONFIG["model"]["temperature"]
MAX_TOKENS = CONFIG["model"]["max_tokens"]

CHATBOT_NOM = CONFIG["chatbot"]["nom"]
CHATBOT_LANGUE = CONFIG["chatbot"]["langue"]

CHEMIN_DATA = RACINE / "data"
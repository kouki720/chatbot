import requests
from langchain.tools import tool


@tool
def raconter_blague() -> str:
    """Raconte une blague courte pour détendre l'atmosphère."""
    try:
        r = requests.get(
            "https://v2.jokeapi.dev/joke/Any?type=single",
            timeout=5,
        )
        r.raise_for_status()
        data = r.json()
        return data.get("joke", "Je n'ai pas de blague sous la main...")
    except Exception:
        return "Je n'arrive pas à trouver une blague pour le moment."
import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()


@tool
def chercher_sujet(categorie: str = "general") -> str:
    """Propose un sujet de conversation à partir des actualités tendance.
    Catégories possibles : general, sports, entertainment, technology, etc.
    """
    api_key = os.getenv("GNEWS_API_KEY")
    if not api_key:
        return "La clé GNews n'est pas configurée."

    try:
        r = requests.get(
            "https://gnews.io/api/v4/top-headlines",
            params={
                "category": categorie,
                "lang": "fr",
                "max": 3,
                "apikey": api_key,
            },
            timeout=5,
        )
        r.raise_for_status()
        articles = r.json().get("articles", [])
        if not articles:
            return "Aucune actualité trouvée pour cette catégorie."
        titres = [f"- {a['title']}" for a in articles]
        return "Titres récents :\n" + "\n".join(titres)
    except Exception:
        return "Je n'arrive pas à récupérer les actualités pour le moment."
import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain.tools import tool

load_dotenv()


@tool
def chercher_web(query: str) -> str:
    """Recherche des informations récentes sur le web. Utile pour les actualités ou les faits vérifiables."""
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "La clé Tavily n'est pas configurée."

    try:
        search = TavilySearch(max_results=3, api_key=api_key)
        reponse = search.invoke({"query": query})

        # TavilySearch renvoie un dict avec une clé 'results'
        articles = reponse.get("results", []) if isinstance(reponse, dict) else []
        if not articles:
            return "Aucun résultat trouvé."

        lignes = []
        for r in articles:
            titre = r.get("title", "Sans titre")
            url = r.get("url", "")
            lignes.append(f"- {titre} : {url}")
        return "Résultats :\n" + "\n".join(lignes)
    except Exception as e:
        return f"Erreur de recherche : {e}"
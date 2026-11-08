import math
from langchain.tools import tool


@tool
def calculer(expression: str) -> str:
    """Effectue un calcul mathématique. Accepte les expressions comme '125 * 8' ou '(10 + 5) * 2'."""
    namespace = {
        "abs": abs, "round": round, "max": max, "min": min, "sum": sum,
        "pow": pow, "math": math,
    }
    try:
        resultat = eval(expression, {"__builtins__": {}}, namespace)
        return f"Résultat : {resultat}"
    except Exception as e:
        return f"Erreur de calcul : {e}"
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.tools.chercher_sujet import chercher_sujet

for cat in ["general", "sports", "entertainment"]:
    print(f"--- {cat} ---")
    resultat = chercher_sujet.invoke({"categorie": cat})
    print(resultat)
    print()
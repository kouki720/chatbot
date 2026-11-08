import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.graph.builder import construire_graphe

graphe = construire_graphe()
config = {"configurable": {"thread_id": "test-outils"}}

cas = [
    "Je m'ennuie, raconte-moi une blague.",
    "Combien font 125 fois 8 ?",
    "Tu connais l'actualité récente sur l'IA ?",
    "Propose-moi un sujet de conversation.",
]

for msg in cas:
    r = graphe.invoke({"messages": [("user", msg)]}, config=config)
    print(f"[user] {msg}")
    print(f"[bot ] {r['messages'][-1].content}\n")
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.graph.builder import construire_graphe

graphe = construire_graphe()

resultat = graphe.invoke({
    "messages": [("user", "Salut, comment ça va ?")]
})

for msg in resultat["messages"]:
    print(f"[{msg.type}] {msg.content}")
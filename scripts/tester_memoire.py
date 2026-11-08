import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.graph.builder import construire_graphe

graphe = construire_graphe()

config = {"configurable": {"thread_id": "conv-1"}}

# Premier message : le bot apprend le prénom
r1 = graphe.invoke(
    {"messages": [("user", "Je m'appelle Karim.")]},
    config=config,
)
print("1er :", r1["messages"][-1].content)

# Deuxième message : le bot doit se souvenir du prénom
r2 = graphe.invoke(
    {"messages": [("user", "Tu te souviens de mon prénom ?")]},
    config=config,
)
print("2e  :", r2["messages"][-1].content)

# Nouveau thread : le bot ne doit plus se souvenir
config2 = {"configurable": {"thread_id": "conv-2"}}
r3 = graphe.invoke(
    {"messages": [("user", "Tu te souviens de mon prénom ?")]},
    config=config2,
)
print("3e  :", r3["messages"][-1].content)
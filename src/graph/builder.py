from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from src.graph.state import EtatChat
from src.graph.nodes import noeud_agent, noeud_outils


def routeur(etat: EtatChat) -> str:
    dernier = etat["messages"][-1]
    if getattr(dernier, "tool_calls", None):
        return "outils"
    return END


def construire_graphe():
    graphe = StateGraph(EtatChat)
    graphe.add_node("agent", noeud_agent)
    graphe.add_node("outils", noeud_outils)
    graphe.add_edge(START, "agent")
    graphe.add_conditional_edges("agent", routeur, {"outils": "outils", END: END})
    graphe.add_edge("outils", "agent")
    return graphe.compile(checkpointer=InMemorySaver())
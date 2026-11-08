from langchain_core.messages import ToolMessage

from src.config import MODEL_ID, TEMPERATURE, MAX_TOKENS, CHATBOT_NOM
from src.llm.nvidia_client import creer_client
from src.graph.state import EtatChat
from src.tools.registre import OUTILS

_PROMPT_SYSTEME = f"""Tu es {CHATBOT_NOM}, un ami avec qui on discute.
Tu réponds de façon naturelle, chaleureuse et concise.
Tu peux utiliser tes outils si c'est pertinent :
- raconter_blague : si l'ambiance est légère ou que l'utilisateur s'ennuie.
- chercher_sujet : si la conversation s'essouffle.
- calculer : pour toute opération mathématique.
- chercher_web : pour des informations récentes ou vérifiables.
"""

_OUTILS_PAR_NOM = {o.name: o for o in OUTILS}


def noeud_agent(etat: EtatChat) -> dict:
    llm = creer_client(MODEL_ID, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
    llm_avec_outils = llm.bind_tools(OUTILS)
    messages = [("system", _PROMPT_SYSTEME)] + etat["messages"]
    reponse = llm_avec_outils.invoke(messages)
    return {"messages": [reponse]}


def noeud_outils(etat: EtatChat) -> dict:
    resultats = []
    for appel in etat["messages"][-1].tool_calls:
        outil = _OUTILS_PAR_NOM[appel["name"]]
        resultat = outil.invoke(appel["args"])
        resultats.append(ToolMessage(content=str(resultat), tool_call_id=appel["id"]))
    return {"messages": resultats}
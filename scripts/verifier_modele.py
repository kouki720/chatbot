import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import MODEL_ID
from src.llm.nvidia_client import creer_client, lister_modeles


def main():
    modeles = lister_modeles()
    print(f"{len(modeles)} modèles disponibles.")
    if MODEL_ID not in modeles:
        print(f"ATTENTION : {MODEL_ID} absent de la liste.")
        for m in modeles[:15]:
            print(" -", m)
        return

    llm = creer_client(MODEL_ID)
    reponse = llm.invoke("Dis bonjour en une phrase courte.")
    print("Réponse :", reponse.content)


if __name__ == "__main__":
    main()
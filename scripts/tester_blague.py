import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.tools.raconter_blague import raconter_blague

print("Appel de raconter_blague...")
resultat = raconter_blague.invoke({})
print("Résultat :", resultat)
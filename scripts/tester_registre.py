import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.tools.registre import OUTILS

for o in OUTILS:
    print(f"- {o.name} : {o.description[:60]}...")
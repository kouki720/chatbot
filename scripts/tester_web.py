import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.tools.chercher_web import chercher_web

print("--- recherche 1 ---")
print(chercher_web.invoke({"query": "actualité intelligence artificielle 2026"}))
print()

print("--- recherche 2 ---")
print(chercher_web.invoke({"query": "dernier film de Christopher Nolan"}))
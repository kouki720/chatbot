import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.tools.calculer import calculer

cas = ["125 * 8", "(10 + 5) * 2", "2 ** 10", "round(3.14159, 2)"]
for c in cas:
    print(f"--- {c} ---")
    print(calculer.invoke({"expression": c}))
    print()
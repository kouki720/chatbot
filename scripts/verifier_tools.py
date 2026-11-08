import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from src.config import NVIDIA_API_KEY

client = ChatNVIDIA(api_key=NVIDIA_API_KEY)
tool_models = [m.id for m in client.get_available_models() if m.supports_tools]
print(f"{len(tool_models)} modèles supportent les outils :")
for m in tool_models[:10]:
    print(" -", m)
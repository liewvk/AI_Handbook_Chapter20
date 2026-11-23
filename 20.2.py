import json
from urllib.error import URLError
from urllib.request import urlopen
 
url = "http://localhost:11434/api/tags"
try:
    with urlopen(url, timeout=10) as response:
        data = json.load(response)
    models = [item["name"] for item in data.get("models", [])]
    print("Installed models:")
    for name in models:
        print("-", name)
    if not models:
        print("No models installed yet.")
except URLError as exc:
    print("Cannot connect to the local Ollama service:", exc)


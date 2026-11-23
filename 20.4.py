import json
from urllib.request import Request, urlopen
 
MODEL = "qwen3.5:4b"
payload = {
    "model": MODEL,
    "messages": [{"role": "user", "content": "Define supervised learning briefly."}],
    "stream": False,
}
request = Request(
    "http://localhost:11434/api/chat",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urlopen(request, timeout=120) as response:
    result = json.load(response)
print(result["message"]["content"])


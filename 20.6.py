from ollama import chat
 
MODEL = "llama3.2:3b"
stream = chat(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain gradient descent to a beginner."}],
    stream=True,
)
for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
print()


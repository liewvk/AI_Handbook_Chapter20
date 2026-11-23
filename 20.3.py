from ollama import chat
 
MODEL = "qwen3.5:4b"  # Replace with a name from ollama list
response = chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Explain AI concepts in simple English."},
        {"role": "user", "content": "What is a neural network? Answer in three sentences."},
    ],
)
print(response.message.content)


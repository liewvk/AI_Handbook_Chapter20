from ollama import chat
 
MODEL = "llama3.2:3b"
question = "Give one practical use of machine learning."
for temperature in (0.0, 0.8):
    response = chat(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        options={"temperature": temperature, "num_predict": 80},
    )
    print("Temperature:", temperature)
    print(response.message.content, "\n")


from ollama import chat
 
MODEL = "llama3.2:3b"
history = [{"role": "system", "content": "You are a concise AI tutor."}]
 
for question in ["What is overfitting?", "Give one way to reduce it."]:
    history.append({"role": "user", "content": question})
    response = chat(model=MODEL, messages=history)
    answer = response.message.content
    print("User:", question)
    print("Assistant:", answer, "\n")
    history.append({"role": "assistant", "content": answer})


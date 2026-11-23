# AI Handbook – Chapter 20

Python examples for Chapter 20 of the AI Handbook. The scripts demonstrate local model size calculations and interactions with [Ollama](https://ollama.com/) using either Ollama's Python package or Ollama's HTTP API.

## Prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com/) running locally on `http://localhost:11434`
- The models used by the examples:
  - `qwen3.5:4b`
  - `llama3.2:3b`

Install Ollama's Python package for the examples that import `ollama`:

```bash
pip install ollama
```

Pull the example models:

```bash
ollama pull qwen3.5:4b
ollama pull llama3.2:3b
```

## Examples

| File | Description |
| --- | --- |
| `20.1.py` | Calculates the raw storage size of a 3-billion-parameter model using 4-bit weights. |
| `20.2.py` | Lists models installed in a local Ollama instance. |
| `20.3.py` | Sends a short system-and-user chat prompt through the Ollama Python package. |
| `20.4.py` | Calls Ollama's `/api/chat` HTTP endpoint to request a supervised-learning definition. |
| `20.5.py` | Maintains a short conversation history across multiple prompts. |
| `20.6.py` | Streams an Ollama response while it is being generated. |
| `20.7.py` | Compares two temperature settings for the same prompt. |
| `AI_Handbook_Chapter20.py` | Main project entry point, currently empty. |

## Running the examples

Start Ollama, ensure the required models are available, and run a script from the repository directory:

```bash
python 20.1.py
python 20.2.py
python 20.3.py
```

The scripts that use Ollama's Python package require `ollama` to be installed. Scripts `20.2.py` and `20.4.py` use Python's standard library and can run without the Ollama Python package.

## Notes

- The model names in several scripts can be changed to any installed Ollama model.
- Ollama must be running locally before executing examples `20.2.py` through `20.7.py`.
- `20.1.py` describes raw parameter storage and does not account for runtime, cache, or framework overhead.

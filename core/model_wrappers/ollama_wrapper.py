import requests

def query_ollama(prompt, model="mistral"):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })

    data = response.json()
    return data.get("response", "").strip()

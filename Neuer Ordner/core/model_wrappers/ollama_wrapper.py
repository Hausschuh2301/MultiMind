<<<<<<< HEAD
import requests

def query_ollama(prompt, model="mistral"):
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }, timeout=30)
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"⚠️ Fehler bei {model}: {str(e)}"
=======
import os
import yaml

def query_ollama(prompt):
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'configs', 'models.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    ollama_config = config.get("models", {}).get("ollama", {})
    if not ollama_config.get("enabled", False):
        return "Ollama ist deaktiviert."

    model_name = ollama_config.get("model_name", "llama3")

    # Simulierte Antwort
    return f"[Simulierte Ollama-Antwort mit Modell '{model_name}' auf: '{prompt}']"
>>>>>>> 131c861 (Buffixes // Fix OpenAI wrapper for openai v0.28.0 compatibility)

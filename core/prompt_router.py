import os
import yaml
from core.memory_manager import add_to_history
from core.model_wrappers.openai_wrapper import query_openai
from core.model_wrappers.claude_wrapper import query_claude
from core.model_wrappers.ollama_wrapper import query_ollama

def load_model_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'models.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config["models"]

def collect_model_outputs(prompt):
    config = load_model_config()
    responses = {}

    if config.get("openai", {}).get("enabled", False):
        responses["OpenAI"] = query_openai(prompt)

    if config.get("claude", {}).get("enabled", False):
        responses["Claude"] = query_claude(prompt)

    if config.get("ollama_mistral", {}).get("enabled", False):
        responses["Mistral (local)"] = query_ollama(prompt, config["ollama_mistral"]["model"])

    if config.get("ollama_llama3", {}).get("enabled", False):
        responses["LLaMA3 (local)"] = query_ollama(prompt, config["ollama_llama3"]["model"])

    return responses

def summarize_responses(prompt, responses):
    config = load_model_config()
    summary_prompt = "Fasse die folgenden Antworten zu einer einzigen, hilfreichen Antwort zusammen:\n\n"
    for name, response in responses.items():
        summary_prompt += f"{name} sagt:\n{response}\n\n"

    # Zusammenfasser-Priorität: OpenAI > Claude > Ollama
    if config.get("openai", {}).get("enabled", False):
        summary = query_openai(summary_prompt)
    elif config.get("claude", {}).get("enabled", False):
        summary = query_claude(summary_prompt)
    elif config.get("ollama_mistral", {}).get("enabled", False):
        summary = query_ollama(summary_prompt, config["ollama_mistral"]["model"])
    else:
        summary = "Keine aktiven Modelle zur Zusammenfassung konfiguriert."

    add_to_history(prompt, responses, summary)
    return summary
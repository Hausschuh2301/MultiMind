<<<<<<< HEAD
import anthropic
import yaml

def query_claude(prompt):
    with open("configs/models.yaml", "r") as f:
        config = yaml.safe_load(f)["claude"]

    client = anthropic.Anthropic(api_key=config["api_key"])
    response = client.messages.create(
        model=config["model"],
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text.strip()
=======
import os
import yaml

def query_claude(prompt):
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'configs', 'models.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    claude_config = config.get("models", {}).get("claude", {})
    if not claude_config.get("enabled", False):
        return "Claude ist deaktiviert."

    # Simulierte Antwort
    return f"[Simulierte Claude-Antwort auf: '{prompt}']"
>>>>>>> 131c861 (Buffixes // Fix OpenAI wrapper for openai v0.28.0 compatibility)

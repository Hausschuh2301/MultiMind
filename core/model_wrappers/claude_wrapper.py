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

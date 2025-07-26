import os
import yaml
import openai

def query_openai(prompt):
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'configs', 'models.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    openai_config = config.get("models", {}).get("openai", {})
    if not openai_config.get("enabled", False):
        return "OpenAI ist deaktiviert."

    api_key = openai_config.get("api_key", "")
    if not api_key or api_key == "...":
        return "Kein gültiger OpenAI API-Schlüssel vorhanden."

    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Du bist ein hilfreicher KI-Assistent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Fehler bei OpenAI: {str(e)}"
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

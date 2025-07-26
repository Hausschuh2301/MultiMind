import openai
import yaml

def query_openai(prompt):
    with open("configs/models.yaml", "r") as f:
        config = yaml.safe_load(f)["openai"]

    openai.api_key = config["api_key"]

    response = openai.ChatCompletion.create(
        model=config["model"],
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

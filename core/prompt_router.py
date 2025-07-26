from core.model_wrappers.openai_wrapper import query_openai
from core.model_wrappers.claude_wrapper import query_claude
from core.memory_manager import add_to_history

def collect_model_outputs(prompt):
    responses = {
        "Ollama (Mistral)": query_ollama(prompt),
        "OpenAI": query_openai(prompt),
        "Claude": query_claude(prompt)
    }
    return responses

def summarize_responses(prompt, responses):
    summary_prompt = "Fasse die folgenden Antworten zu einer klaren, hilfreichen Antwort zusammen:\n\n"
    for name, response in responses.items():
        summary_prompt += f"{name} sagt:\n{response}\n\n"

    final_answer = query_openai(summary_prompt)  # GPT als Zusammenfasser
    add_to_history(prompt, responses, final_answer)
    return final_answer

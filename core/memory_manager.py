conversation_history = []

def add_to_history(prompt, responses, final_answer):
    conversation_history.append({
        "prompt": prompt,
        "responses": responses,
        "final": final_answer
    })

def get_history():
    return conversation_history

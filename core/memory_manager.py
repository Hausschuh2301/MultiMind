import datetime

conversation_history = []

def add_to_history(prompt, final_answer, timestamp=None):
    if timestamp is None:
        timestamp = datetime.datetime.now()
    conversation_history.append({
        "prompt": prompt,
        "final": final_answer,
        "timestamp": timestamp
    })

def get_history():
    return conversation_history
import streamlit as st
from core.prompt_router import collect_model_outputs, summarize_responses
from core.memory_manager import get_history

st.title("🧠 MULTIMIND - KI-Ensemble")

prompt = st.text_area("Deine Frage", height=150)

if st.button("Antwort generieren"):
    with st.spinner("Die Modelle denken nach..."):
        responses = collect_model_outputs(prompt)
        final = summarize_responses(prompt, responses)

    st.subheader("Antworten der Modelle:")
    for name, res in responses.items():
        st.markdown(f"**{name}**:\n{res}")

    st.subheader("🧠 Zusammenfassung")
    st.success(final)

st.sidebar.title("Verlauf")
for entry in get_history():
    st.sidebar.markdown(f"**Frage:** {entry['prompt']}")
    st.sidebar.markdown(f"**Antwort:** {entry['final']}")

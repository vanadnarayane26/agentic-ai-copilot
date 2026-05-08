import streamlit as st

from chat.memory import initialize_memory, add_message
from llm.ollama_client import generate_response


st.set_page_config(
    page_title="Agentic AI Copilot",
    layout="wide",
)

st.title("Agentic AI Copilot V1.0")

initialize_memory()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask something...")

if user_input:
    add_message("user", user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        full_response = ""

        stream = generate_response(st.session_state.messages)

        for chunk in stream:
            content = chunk["message"]["content"]

            full_response += content

            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    add_message("assistant", full_response)
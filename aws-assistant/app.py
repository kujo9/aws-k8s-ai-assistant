"""Streamlit chat UI for the AWS assistant.

"""

import asyncio
import uuid

import streamlit as st

import agent
import config

st.set_page_config(page_title="Kodjo AWS Assistant", layout="centered")
st.title("Kodjo AWS Assistant")
st.caption(f"Your AWS account, home Region {config.REGION}. I can inspect, explain, and suggest, but changes happen only with your approval. ")

# One chat per browser tab. The agent keeps the full history under chat_id;
# this list is only what the page shows. A page refresh starts a new chat.
if "chat_id" not in st.session_state:
    st.session_state.chat_id = str(uuid.uuid4())
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask about your AWS account")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Working..."):
            answer, called = asyncio.run(agent.ask(question, st.session_state.chat_id))

        if called:
            st.caption("Tools called: " + ", ".join(called))
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
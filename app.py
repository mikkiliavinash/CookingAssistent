import streamlit as st
from pprint import pprint

from langchain.messages import HumanMessage
from agent import cooking_agent

st.set_page_config(page_title="Chef Buddy", page_icon="🍳")

st.title("🍳 Chef Buddy")

# Create one thread per browser session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "1"

# UI chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask a cooking question...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )
    config = { "configurable": {  "thread_id": st.session_state.thread_id}}
    # Call the agent
    result = cooking_agent.invoke(
        {
            "messages": [
                HumanMessage(content=prompt)
            ]
        },
        config=config
    )


    response = result["messages"][-1].content

    if isinstance(response, list):
        response = response[0]["text"]

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
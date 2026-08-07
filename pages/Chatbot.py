import streamlit as st
import ollama
import time

MODEL = "qwen2.5:0.5b"

st.logo(image="https://i.ytimg.com/vi/XAIkWgrC6o0/sddefault.jpg", size="large",
        link="https://www.youtube.com/watch?v=9PGspaFVpec&list=RD9PGspaFVpec&start_radio=1")
st.title("My AI Chatbot")
st.markdown(
    """
    Hello! I tried kinda hard on this

    **👇:rainbow[PLEASE] help support me**
    """
)
st.link_button("My CodeTorch account", "https://codetorch.net/en/users/Y7bnb", icon="🔥", icon_position="right")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        temp = ollama.chat(model=MODEL, messages=st.session_state.messages)
        assistant_response = temp["message"]["content"]
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
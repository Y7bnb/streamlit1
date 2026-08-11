import streamlit as st
st.markdown(
    """
    **👇:rainbow[PLEASE] help support me**
    """
)
st.link_button("My CodeTorch account", "https://codetorch.net/en/users/Y7bnb", icon="🔥", icon_position="right")

st.title(":rainbow[Y7bnb's] 1st app!")
st.page_link("pages/Chatbot.py", label="**:rainbow[ChatBot]**", icon="🤖")
st.page_link("pages/Chatroom.py", label="**:rainbow[Chatroom]**", icon="💬")
st.page_link("pages/Temperature_Convertor.py", label="**Celsius to Fahrenheit Convertor**", icon="🌡️", disabled=True)
import streamlit as st

pages = {
    "Web": [
        st.Page("pages/Home.py", title="**:rainbow[Home]**", icon="🏠", default=True)
    ],
    "Artificial Intelligence": [
        st.Page("pages/Chatbot.py", title="**:rainbow[ChatBot]**", icon="🤖"),
        st.Page("pages/RAG_System.py", title="**:rainbow[RAG System]**", icon="📝"),
    ],
    "Utilities": [
        st.Page("pages/BG_Remover.py", title="**:rainbow[BG Remover]**", icon="🌇", visibility="hidden"),
        st.Page("pages/Chatroom.py", title="**:rainbow[Chatroom]**", icon="💬"),
        st.Page("pages/QR-Code_Generator.py", title="**:rainbow[QR-Code Generator]**", icon="🔲"),
        st.Page("pages/Temperature_Convertor.py", title="**Celsius to Fahrenheit Convertor**", icon="🌡️", visibility="hidden"),
        st.Page("pages/Weather.py", title="**:rainbow[Weather]**", icon="🌦️"),
        st.Page("pages/Image_Enhancer.py", title="**:rainbow[Image Enhancer]**", icon="🌇"),
        st.Page("pages/Text_to_Speech.py", title="**:rainbow[Text to Speech]**", icon="💬"),
    ],
}

pg = st.navigation(pages)
pg.run()
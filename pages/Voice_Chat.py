import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.set_page_config(page_title="Voice Chat")

st.title("🎙️ Voice Chat")

st.write("Click START and allow microphone access.")

webrtc_streamer(key="voice-chat", sendback_audio=True, media_stream_constraints={"video": False, "audio": True,})

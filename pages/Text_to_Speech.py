import streamlit as st

import sys

import pyttsx3

tts = pyttsx3.init()  # Initialize the TTS engine.

st.set_page_config(layout="wide", page_title="Text to Speech")
st.title("Text to Speech")

voices = tts.getProperty('voices')
# for index, voice in enumerate(voices):
#   st.write(f'ID: {voice.id} | Name: {voice.name}')
voice = st.number_input("Voice ID", min_value=0, max_value=len(voices) - 1, value=19)
tts.setProperty('voice', voices[voice].id)

st.write('Enter the text to speak.')
text = st.text_input("Enter text: ")

tts.say(text)  # Add some text for the TTS engine to say.
tts.runAndWait()  # Make the TTS engine say it.

# import streamlit as st
# from gtts import gTTS
# from io import BytesIO
# 
# st.title("Text to Speech")
#
# text = st.text_input("Enter text:")
# voices = {
#     "English (US)": "com",
#     "English (UK)": "co.uk",
#     "English (Australia)": "com.au",
#     "English (India)": "co.in",
#     "English (Ireland)": "ie"
# }
#
# choice = st.selectbox("Choose an accent:", list(voices.keys()))
#
# if st.button("Generate Speech"):
#     if text.strip():
#         try:
#             speech = gTTS(text=text, lang="en", tld=voices[choice], slow=False)
#
#             audio_buffer = BytesIO()
#             speech.write_to_fp(audio_buffer)
#             audio_buffer.seek(0)
#
#             st.audio(audio_buffer, format="audio/mp3")
#
#         except Exception as e:
#             st.error(f"Error generating speech: {e}")
#     else:
#         st.warning("Please enter some text.")
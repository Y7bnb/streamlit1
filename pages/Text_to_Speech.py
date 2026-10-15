import streamlit as st

import sys

import pyttsx3

tts = pyttsx3.init()  # Initialize the TTS engine.

st.set_page_config(layout="wide", page_title="Text to Speech")
st.title("Text to Speech")

voices = tts.getProperty('voices')
# for index, voice in enumerate(voices):
#   st.write(f'ID: {voice.id} | Name: {voice.name}')
voice = st.number_input("Voice ID", min_value=0, max_value=len(voices), value=19)
tts.setProperty('voice', voices[voice].id)

st.write('Enter the text to speak.')
text = st.text_input("Enter text: ")

tts.say(text)  # Add some text for the TTS engine to say.
tts.runAndWait()  # Make the TTS engine say it.
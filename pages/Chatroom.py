import threading

import streamlit as st


@st.cache_resource
def get_room():
    return {"messages": [], "lock": threading.Lock()}


room = get_room()

st.logo(
    image="https://i.ytimg.com/vi/XAIkWgrC6o0/sddefault.jpg",
    size="large",
    link="https://www.youtube.com/watch?v=9PGspaFVpec&list=RD9PGspaFVpec&start_radio=1",
)

st.title("Chat room")

if "name" not in st.session_state:
    with st.form("join"):
        name = st.text_input("Display name")

        if st.form_submit_button("Join") and name.strip():
            st.session_state.name = name.strip()
            st.rerun()

    st.stop()

st.caption(f"Chatting as {st.session_state.name}")


@st.fragment(run_every=1)
def show_messages():
    for m in room["messages"]:
        with st.chat_message("user" if m["name"] == st.session_state.name else "assistant"):
            st.markdown(m["name"])

            if "text" in m:
                st.markdown(m["text"])

            elif "audio_file" in m:
                st.audio(m["audio_file"], format="audio/wav")

            elif "files" in m:
                st.image(m["files"])


show_messages()

message = st.chat_input("Message", accept_file=True, file_type=["jpg", "jpeg", "png"], accept_audio=True)

if message:
    if message.text:
        with room["lock"]:
            room["messages"].append(
                {
                    "name": st.session_state.name,
                    "text": message.text,
                }
            )

        st.rerun()

    if message.audio:
        # Convert the uploaded audio to bytes before
        # putting it into the shared room state.
        audio_bytes = message.audio.getvalue()

        with room["lock"]:
            room["messages"].append(
                {
                    "name": st.session_state.name,
                    "audio_file": audio_bytes,
                }
            )

        st.rerun()

    if message["files"]:
        with room["lock"]:
            room["messages"].append(
                {
                    "name": st.session_state.name,
                    "files": message["files"],
                }
            )

        st.rerun()

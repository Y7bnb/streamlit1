import streamlit as st
from rembg import remove
from PIL import Image

st.title("Background Remover")

image = st.file_uploader("Upload your Photo", type=["jpg", "png", "jpeg"])

if image is not None:
    bg_button = st.button("Remove Background")
    if bg_button:
        with st.spinner("Removing background..."):
            input_image = Image.open(image)

            output_image = remove(input_image)

            st.image(output_image, caption="Right click and save the new image!")
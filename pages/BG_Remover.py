import streamlit as st
from rembg import remove, new_session
from PIL import Image

@st.cache_resource
def load_rembg_model():
    # By default, this loads the 'u2net' model (~176MB)
    return new_session(model_name="u2net")

st.title("Background Remover")

rembg_session = load_rembg_model()

image = st.file_uploader("Upload your Photo", type=["png", "jpg", "jpeg"])

if image is not None:
    input_image = Image.open(image)

    col1, col2 = st.columns(2)

    with col1:
        st.header("Original Image")
        st.image(input_image, caption="Original Image", use_container_width=True)

    bg_button = st.button("Remove Background")

    if bg_button:
        with st.spinner("Removing background..."):
            with col2:
                st.header("Removed Background")
                output_image = remove(input_image)

                st.image(output_image, use_container_width=True, caption="Right click and save the new image!")


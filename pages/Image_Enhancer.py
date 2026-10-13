import streamlit as st
from PIL import Image, ImageEnhance

# Set up page configurations
st.set_page_config(layout="wide", page_title="Image Enhancer App")
st.title("📸 Photo Enhancer App")
st.write("Upload an image and use the sidebar sliders to tune its properties.")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Enhancement Settings")

# Sliders map to Pillow's enhancement factor scale (1.0 is default)
def reset_sliders():
    st.session_state.brightness = 1.0
    st.session_state.contrast = 1.2
    st.session_state.color = 1.3
    st.session_state.sharpness = 1.5

brightness_factor = st.sidebar.slider("Brightness", min_value=0.0, max_value=3.0, value=1.0, step=0.1, key="brightness")
contrast_factor = st.sidebar.slider("Contrast", min_value=0.0, max_value=3.0, value=1.0, step=0.1, key="contrast")
color_factor = st.sidebar.slider("Color / Saturation", min_value=0.0, max_value=3.0, value=1.0, step=0.1, key="color")
sharpness_factor = st.sidebar.slider("Sharpness", min_value=0.0, max_value=3.0, value=1.0, step=0.1, key="sharpness")

st.sidebar.button("Reset", on_click=reset_sliders)

# --- IMAGE UPLOADER ---
uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image via Pillow
    original_img = Image.open(uploaded_file)

    # --- IMAGE PROCESSING ---
    # Sequential application of filters matching slider values
    modified_img = ImageEnhance.Brightness(original_img).enhance(brightness_factor)
    modified_img = ImageEnhance.Contrast(modified_img).enhance(contrast_factor)
    modified_img = ImageEnhance.Color(modified_img).enhance(color_factor)
    modified_img = ImageEnhance.Sharpness(modified_img).enhance(sharpness_factor)

    # --- DISPLAY LAYOUT ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(original_img)

    with col2:
        st.subheader("Enhanced Image")
        st.image(modified_img, caption="Right click image to download!")
else:
    st.info("💡 Please upload a JPG or PNG image to start tweaking values.")

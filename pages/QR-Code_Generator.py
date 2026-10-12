import streamlit as st
import qrcode
from PIL import Image

st.set_page_config(layout="wide", page_title="QR-Code Generator")
st.title("QR Code Generator")

link = st.text_input("Enter the link here")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=2,
)
qr.add_data(link)
# qr.make(fit=True)

img = qr.make_image().get_image()

st.image(img, caption=link)
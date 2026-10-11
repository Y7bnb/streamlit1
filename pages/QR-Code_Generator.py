import streamlit as st
import segno

st.title("QR-Code Generator")

link = st.text_input("Paste link here")
qrcode = segno.make_qr(link)
qrcode.save("qrcode.png", scale=6, border=2)
st.image("qrcode.png")

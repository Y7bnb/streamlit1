import streamlit as st

st.title("Celsius to Fahrenheit Converter")
st.markdown(
    """
    **:rainbow[I tried]**
    """
)

celsius = st.slider("Select temperature in Celsius:", min_value=-90, max_value=60, value=0)
fahrenheit = (celsius * 9/5) + 32
if st.button("Convert to Fahrenheit"):
    st.write(f"{celsius}°C is equal to {fahrenheit}°F")
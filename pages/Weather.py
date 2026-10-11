import streamlit as st
import asyncio
import python_weather


# Define an async function to interact with python_weather
async def fetch_weather(city: str, units: str):
    # Set the measurement unit system
    unit_system = python_weather.METRIC if units == "Celsius (°C)" else python_weather.IMPERIAL

    # Initialize the asynchronous client
    async with python_weather.Client(unit=unit_system) as client:
        # Fetch weather data for the specified location
        weather = await client.get(city)
        return weather


# --- Streamlit UI Setup ---
st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

st.title("🌤️ Real-Time Weather App")

# User Inputs
city_input = st.text_input("Enter City Name:", placeholder="e.g., Vancouver, New York, Tokyo")
unit_choice = st.radio("Select Temperature Unit:", ["Celsius (°C)", "Fahrenheit (°F)"], horizontal=True)

if city_input:
    with st.spinner(f"Fetching current weather for {city_input}..."):
        try:
            # Execute the async function synchronously using asyncio.run
            weather_data = asyncio.run(fetch_weather(city_input, unit_choice))

            # --- Main Weather Display ---
            st.success(f"Weather data retrieved for **{city_input.title()}**!")

            col1, col2 = st.columns(2)
            with col1:
                st.metric(
                    label="Current Temperature",
                    value=f"{weather_data.temperature}°"
                )
            with col2:
                # Capitalize description text safely
                desc = getattr(weather_data, 'description', 'N/A')
                st.markdown(f"### **Condition**\n{desc.title()}")

            # --- Extended Daily Forecasts ---
            st.markdown("---")
            st.subheader("📅 3-Day Forecast Overview")

            # Grid display for upcoming days
            forecast_cols = st.columns(3)

            # python_weather allowing direct loop iteration over daily forecasts
            for index, daily in enumerate(list(weather_data)[:3]):
                with forecast_cols[index]:
                    st.markdown(f"**{daily.date}**")
                    st.markdown(f"🌡️ Temp: **{daily.temperature}°**")

        except Exception as e:
            st.error(f"⚠️ Unable to find weather details for '{city_input}'. Please check the spelling.")
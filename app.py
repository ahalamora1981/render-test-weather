import streamlit as st
import requests

# Dictionary of major Chinese cities with their coordinates (Latitude, Longitude)
CITIES = {
    "Beijing": {"lat": 39.9042, "lon": 116.4074},
    "Shanghai": {"lat": 31.2304, "lon": 121.4737},
    "Guangzhou": {"lat": 23.1291, "lon": 113.2644},
    "Shenzhen": {"lat": 22.5431, "lon": 114.0579},
    "Chengdu": {"lat": 30.5728, "lon": 104.0668},
    "Xi'an": {"lat": 34.3416, "lon": 108.9398},
    "Hangzhou": {"lat": 30.2741, "lon": 120.1551},
    "Wuhan": {"lat": 30.5928, "lon": 114.3055},
    "Nanjing": {"lat": 32.0603, "lon": 118.7969},
    "Chongqing": {"lat": 29.5630, "lon": 106.5516}
}

def get_weather(lat, lon):
    """Fetches current weather data from Open-Meteo API."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def main():
    st.set_page_config(page_title="China Weather App", page_icon="🇨🇳")
    
    st.title("🇨🇳 Major Cities Weather in China")
    st.write("Select a city to view its current weather conditions.")

    # City selection
    selected_city = st.selectbox("Choose a city:", list(CITIES.keys()))

    if selected_city:
        coords = CITIES[selected_city]
        
        with st.spinner(f"Fetching weather for {selected_city}..."):
            weather_data = get_weather(coords["lat"], coords["lon"])

        if weather_data and "current_weather" in weather_data:
            current = weather_data["current_weather"]
            
            # Display metrics
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="Temperature", value=f"{current['temperature']} °C")
            
            with col2:
                st.metric(label="Wind Speed", value=f"{current['windspeed']} km/h")
                
            with col3:
                # Weather codes interpretation could be added here for better UX
                # For now, just displaying the code or a simple mapping could be done if requested
                st.metric(label="Wind Direction", value=f"{current['winddirection']}°")
            
            st.success(f"Weather data updated for {selected_city}!")
            
            # Display raw data optionally
            with st.expander("See raw data"):
                st.json(weather_data)
        else:
            st.warning("No weather data available.")

if __name__ == "__main__":
    main()

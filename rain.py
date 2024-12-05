import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model  # For loading Keras model


model = load_model("rainpred1.keras")


location_mapping = {
    "Adelaide": -0.057496, "Albany": 1.213567, "Albury": -0.248093, "AliceSprings": -2.172955,
    "Ballarat": 0.590818, "Bendigo": -0.536307, "Brisbane": 0.045406, "Cairns": 1.460609,
    "Canberra": -0.564575, "CoffsHarbour": 1.089804, "Dartmoor": 1.365389, "Darwin": 0.746116,
    "GoldCoast": 0.559938, "Hobart": 0.300210, "Launceston": 0.168789, "Melbourne": -0.312300,
    "MelbourneAirport": -0.033334, "Mildura": -1.728441, "MountGambier": 1.306208,
    "MountGinini": 0.786392, "MountSprings": -1.029307, "Newcastle": 0.334721, "NorfolkIsland": 1.349790,
    "Perth": -0.268199, "PerthAirport": -0.480510, "Penrith": -0.365459, "Richmond": -0.516908,
    "Sale": -0.085331, "Sydney": 0.618423, "SydneyAirport": 0.595831, "Tuggeranong": -0.504465,
    "WaggaWagga": -0.641701, "Witchcliffe": 1.141801, "Wollongong": 0.240843, "Williamtown": 0.211052,
    "Woomera": -2.378405
}

wind_directiongust = {
    "N": 1.056246, "NNE": 0.168212, "NE": -0.819096, "ENE": -1.440791, "E": -1.725326,
    "ESE": -1.348804, "SE": 0.754542, "SSE": -0.687142, "S": 0.020536, "SSW": -0.047826,
    "SW": -0.429853, "WSW": 0.257421, "W": 0.754542, "WNW": 1.353028, "NW": 1.485132, "NNW": 1.490119
}

wind_direction9am = {key: value for key, value in wind_directiongust.items()}
wind_direction3pm = {key: value for key, value in wind_directiongust.items()}
st.markdown("""
    <style>
        /* Body styling */
        body {
            background-color: #F0F8FF;  /* Soft light blue background */
            color: #2F4F4F;  /* Dark slate gray font color */
            font-family: 'Arial', sans-serif;  /* Clean, modern font */
        }

        /* Title styling */
        .css-18e3th9 {
            font-size: 36px;
            color: #1E90FF;  /* Bright blue for the title */
            font-weight: bold;
            text-align: center;
            padding: 20px 0;
        }

        /* Header styling */
        h1 {
            font-size: 36px;
            font-weight: bold;
            color: #1E90FF;  /* Title color */
            text-align: center;
        }

        /* Button styling */
        .css-1emrehy {
            background-color: #1E90FF;  /* Blue button */
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            transition: background-color 0.3s ease;
        }

        .css-1emrehy:hover {
            background-color: #4682B4;  /* Darker blue when hovered */
        }

        /* Input fields styling */
        .stTextInput>label {
            color: #1E90FF;  /* Blue label for input fields */
            font-size: 18px;
        }

        .stNumberInput>label {
            color: #1E90FF;  /* Blue label for number input fields */
            font-size: 18px;
        }

        .stSelectbox>label {
            color: #1E90FF;  /* Blue label for select boxes */
            font-size: 18px;
        }

        /* Modify the background of the sidebar */
        .css-1d391kg {
            background-color: #F0F8FF;  /* Matching light blue background for sidebar */
        }

        /* Customize the container for the layout */
        .css-1kyxreq {
            background-color: #ffffff;  /* White background for content container */
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Modify the success message color */
        .st-success {
            color: #32CD32;  /* Green color for success messages */
        }

        /* Form control focus styles */
        .stTextInput input:focus, .stNumberInput input:focus, .stSelectbox select:focus {
            border-color: #1E90FF;  /* Focus border color to blue */
            outline: none;
        }

        /* Dropdown select box */
        .stSelectbox select {
            background-color: #F0F8FF;
            color: #2F4F4F;
            border-radius: 5px;
            border: 1px solid #1E90FF;
            padding: 10px;
        }

        /* Customize the page title color */
        h1 {
            color: #1E90FF;
        }
    </style>
""", unsafe_allow_html=True)


def predict_rain(input_data):
    prediction = model.predict(input_data)
    return "Rain will Happen" if prediction[0] == 1 else "No Rain will happen"


def main():
    st.title("🌧️ Rainfall Prediction in Australia🌦️")
    st.write("Predict if it will rain tomorrow based on today's weather conditions.")

    
    location = st.selectbox("📍 Select Location", sorted(location_mapping.keys()))
    
   
    min_temp = st.number_input("🌡️ Min Temp", min_value=-10.0, max_value=50.0, value=15.0)
    max_temp = st.number_input("🌡️ Max Temp", min_value=-10.0, max_value=50.0, value=25.0)
    rainfall = st.number_input("💧 Rainfall", min_value=0.0, max_value=500.0, value=0.0)
    evaporation = st.number_input("💨 Evaporation", min_value=0.0, max_value=50.0, value=6.0)
    sunshine = st.number_input("☀️ Sunshine", min_value=0.0, max_value=15.0, value=8.0)
    wind_gust_dir = st.selectbox("🌬️ Wind Gust Direction", list(wind_directiongust.keys()))
    wind_gust_speed = st.number_input("🌬️ Wind Gust Speed", min_value=0.0, max_value=100.0, value=15.0)
    wind_dir_9am = st.selectbox("🌬️ Wind Direction at 9am", list(wind_direction9am.keys()))
    wind_dir_3pm = st.selectbox("🌬️ Wind Direction at 3pm", list(wind_direction3pm.keys()))
    wind_speed_9am = st.number_input("💨 Wind Speed at 9am", min_value=0.0, max_value=100.0, value=5.0)
    wind_speed_3pm = st.number_input("💨 Wind Speed at 3pm", min_value=0.0, max_value=100.0, value=10.0)
    humidity_9am = st.number_input("💧 Humidity at 9am", min_value=0, max_value=100, value=80)
    humidity_3pm = st.number_input("💧 Humidity at 3pm", min_value=0, max_value=100, value=70)
    pressure_9am = st.number_input("🌡️ Pressure at 9am", min_value=900, max_value=1100, value=1013)
    pressure_3pm = st.number_input("🌡️ Pressure at 3pm", min_value=900, max_value=1100, value=1012)
    cloud_9am = st.number_input("☁️ Cloud at 9am", min_value=0, max_value=100, value=20)
    cloud_3pm = st.number_input("☁️ Cloud at 3pm", min_value=0, max_value=100, value=30)
    temp_9am = st.number_input("🌡️ Temp at 9am", min_value=-10.0, max_value=50.0, value=18.0)
    temp_3pm = st.number_input("🌡️ Temp at 3pm", min_value=-10.0, max_value=50.0, value=22.0)

   
    rain_today = st.selectbox("🌧️ Rain Today (Yes/No)", ["Yes", "No"])
    encoded_rain_today = 1 if rain_today == "Yes" else 0

    # Encode location and wind directions
    encoded_location = location_mapping.get(location, 0)
    encoded_wind_gust_dir = wind_directiongust.get(wind_gust_dir, 0)
    encoded_wind_dir_9am = wind_direction9am.get(wind_dir_9am, 0)
    encoded_wind_dir_3pm = wind_direction3pm.get(wind_dir_3pm, 0)

   
    input_data = pd.DataFrame([{
        'Location': encoded_location,
        'MinTemp': min_temp,
        'MaxTemp': max_temp,
        'Rainfall': rainfall,
        'Evaporation': evaporation,
        'Sunshine': sunshine,
        'WindGustDir': encoded_wind_gust_dir,
        'WindGustSpeed': wind_gust_speed,
        'WindDir9am': encoded_wind_dir_9am,
        'WindDir3pm': encoded_wind_dir_3pm,
        'WindSpeed9am': wind_speed_9am,
        'WindSpeed3pm': wind_speed_3pm,
        'Humidity9am': humidity_9am,
        'Humidity3pm': humidity_3pm,
        'Pressure9am': pressure_9am,
        'Pressure3pm': pressure_3pm,
        'Cloud9am': cloud_9am,
        'Cloud3pm': cloud_3pm,
        'Temp9am': temp_9am,
        'Temp3pm': temp_3pm,
        'RainToday': encoded_rain_today
    }])

    # Predict rainfall
    if st.button("Predict"):
        prediction = predict_rain(input_data)
        st.success(f"The prediction is: {prediction}")

if __name__ == "__main__":
    main()

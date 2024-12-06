import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model  


model = load_model("Ausrain.keras")

location_mapping = {
    "Adelaide": 0.215471, "Albany":0.296711, "Albury": 0.203289 , "AliceSprings": 0.080263 ,
    "Ballarat":0.256908,"Badgerysreek":0.193752, "Bendigo": 0.184868, "Brisbane":0.222048, "Cairns": 0.312500,
    "Canberra": 0.183062 ,"cobar":0.128282,"CoffsHarbour": 0.288800, "Dartmoor": 0.306414, "Darwin":0.266834 ,
    "GoldCoast":0.254934 , "Hobart": 0.238334, "Katherine":0.167934,"Launceston": 0.229934, "Melbourne": 0.199186,
    "MelbourneAirport": 0.217016, "Mildura": 0.108674,"More":0.130941, "MountGambier": 0.302632,
    "MountGinini":0.269408, "MountSprings": -1.029307, "Newcastle": 0.240540,"Nhil":0.153359,"NorahHead":0.268975, "NorfolkIsland": 0.305417,"Nurioopta":0.196743,
    "Perth": 0.202004, "PerthAirport": 0.188435, "Penrith": 0.195788,"PearceRAAF":0.167830,"Portland":0.363908, "Richmond": 0.186108,
    "Sale": 0.213692,"SalmonGums":0.157281, "Sydney": 0.258672 , "SydneyAirport": 0.257228,"Townsville":0.170724, "Tuggeranong": 0.186904,"Uluru":0.073511,
    "WaggaWagga": 0.178132,"Walpole":0.315702, "Watsonia":0.245264,"Witchcliffe":0.292124, "Wollongong": 0.234539 , "Williamtown": 0.232635,
    "Woomera": 0.067132
}


wind_directiongust = {
    "N": 0.263288, "NNE": 0.226176, "NE": 0.186494, "ENE": 0.158934, "E": 0.168673,
    "ESE": 0.162778, "SE": 0.184009, "SSE": 0.190430, "S": 0.220004, "SSW":0.219348,
    "SW": 0.201182, "WSW": 0.219899, "W": 0.250679, "WNW": 0.275691, "NW": 0.281212, "NNW": 0.277764
}
wind_dir3pm = {
    "N": 0.272328, "NNE": 0.239302, "NE": 0.184915, "ENE": 0.175894, "E": 0.147043,
    "ESE": 0.167078, "SE": 0.204699, "SSE": 0.186190, "S":  0.209047, "SSW":0.217147,
    "SW": 0.193286, "WSW": 0.229904, "W": 0.250049, "WNW": 0.270453, "NW":0.273060, "NNW": 0.281420
}
wind_dir9am = {
    "N": 0.243281, "NNE": 0.262886, "NE": 0.204406, "ENE": 0.174196, "E": 0.143309,
    "ESE": 0.146527, "SE": 0.160547, "SSE": 0.175702, "S":0.194133, "SSW":0.216818,
    "SW": 0.226641, "WSW": 0.240888, "W": 0.254995, "WNW": 0.262746, "NW": 0.277933, "NNW": 0.304511
}



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
    return "Rain" if prediction[0] == 1 else "No Rain"


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
    wind_dir_9am = st.selectbox("🌬️ Wind Direction at 9am", list(wind_dir9am.keys()))
    wind_dir_3pm = st.selectbox("🌬️ Wind Direction at 3pm", list(wind_dir3pm .keys()))
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

    
    encoded_location = location_mapping.get(location, 0)
    encoded_wind_gust_dir = wind_directiongust.get(wind_gust_dir, 0)
    encoded_wind_dir_9am = wind_dir9am.get(wind_dir_9am, 0)
    encoded_wind_dir_3pm = wind_dir3pm .get(wind_dir_3pm, 0)

    
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


    if st.button("Predict"):
        prediction = predict_rain(input_data)
        st.success(f"The prediction is: {prediction}")

if __name__ == "__main__":
    main()

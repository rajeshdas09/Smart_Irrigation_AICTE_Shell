import streamlit as st
import numpy as np
import joblib  

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  

st.title("Smart Sprinkler System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# Real Sensor Labels
sensor_labels = [
    "Soil Moisture 1", "Soil Moisture 2", "Soil Moisture 3", "Soil Moisture 4",
    "Temperature 1", "Temperature 2", "Humidity 1", "Humidity 2",
    "Light Intensity 1", "Light Intensity 2", "Water Level", "pH Value",
    "EC Value", "Rain Sensor", "Wind Speed", "Dew Point",
    "Soil Type Index", "Crop Type Index", "Time of Day", "Season Index"
]

sensor_values = []
for i in range(20):
    val = st.slider(sensor_labels[i], min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

# Predict and show color-coded output
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction Result:")
    for i, status in enumerate(prediction):
        color = "green" if status == 1 else "red"
        label = f"Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}"
        st.markdown(f"<span style='color:{color}'>{label}</span>", unsafe_allow_html=True)

# Footer 
st.markdown("---")
st.markdown("Developed by **Rajesh Das** | Smart Irrigation Project")
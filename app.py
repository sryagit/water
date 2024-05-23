import streamlit as st
import joblib
import pandas as pd
from PIL import Image
import requests

#load the model
model = joblib.load("water_potability.joblib")

#Define a function to make predictions
def predict_potability(df):
    prediction = model.predict(df)
    return prediction


#Define the streamlit app
def main():
    #set page title
    st.set_page_config(page_title="Water Potability Prediction App ")

    #Add a title to the app
    st.title("Water Potability Prediction App \U0001F4A7")

    #Add image of water
    image_url = 'https://raw.githubusercontent.com/SatyamedhasP/Water-Potability/main/Water_quality_image.jpg'
    image = Image.open(requests.get(image_url, stream=True).raw)
    st.image(image, use_column_width=True)

    #Add description of the app
    st.write('This app predicts the potability of water (drinkable or not) based on various factors')
    
    #Add sliders for user input
    ph = st.slider('pH value', min_value=0.0, max_value=14.0, step=0.1, value=7.0)
    hardness = st.slider("Hardness", min_value=0, max_value=500, step=1, value=150)
    solids = st.slider("Solids (mg/L)", min_value=0, max_value=50000, step=10, value=2000)
    chloramines = st.slider("Chloramines (ppm)", min_value=0.0, max_value=10.0, step=0.1, value=4.0)
    sulfate = st.slider("Sulfate (mg/L)", min_value=0, max_value=500, step=1, value=250)
    conductivity = st.slider("Conductivity (μS/cm)", min_value=0, max_value=10000, step=10, value=1500)
    organic_carbon = st.slider("Organic Carbon (mg/L)", min_value=0, max_value=100, step=1, value=20)
    trihalomethanes = st.slider("Trihalomethanes (μg/L)", min_value=0.0, max_value=100.0, step=0.1, value=60.0)
    turbidity = st.slider("Turbidity (NTU)", min_value=0.0, max_value=10.0, step=0.1, value=5.0)

    #dictionary of user input
    user_input = {
        'ph':[ph],
        'Hardness':[hardness],
        'Solids':[solids],
        'Chloramines':[chloramines],
        'Sulfate':[sulfate],
        'Conductivity':[conductivity],
        'Organic_carbon':[organic_carbon],
        'Trihalomethanes':[trihalomethanes],
        'Turbidity':[turbidity]
    }

    #Pandas dataframe from user input
    df = pd.DataFrame(user_input)

    #Add button to submit user input and make predictions
    if st.button('Predict'):
        prediction = predict_potability(df)
        st.write('Prediction:')
        if prediction[0]==0:
            st.write('The water is not potable!')
        else:
            st.write('The water is potable!')

#Run the app
if __name__ == '__main__':
    main()

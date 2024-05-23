# Import necessary libraries
import streamlit as st
import joblib

# Load the trained model
model = joblib.load('water_potability_model.joblib')

# Define a function to make predictions
def predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    data = [[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]
    prediction = model.predict(data)
    return prediction[0]

# Create a Streamlit app
def main():
    st.title('Water Potability Prediction')
    st.write('Enter the following parameters to predict water potability:')
    ph = st.slider('pH', 0.0, 14.0, 7.0, 0.1)
    hardness = st.slider('Hardness', 0.0, 400.0, 200.0, 1.0)
    solids = st.slider('Total Solids', 0.0, 5000.0, 2500.0, 10.0)
    chloramines = st.slider('Chloramines', 0.0, 15.0, 5.0, 0.1)
    sulfate = st.slider('Sulfate', 0.0, 500.0, 250.0, 1.0)
    conductivity = st.slider('Conductivity', 0.0, 5000.0, 2500.0, 10.0)
    organic_carbon = st.slider('Organic Carbon', 0.0, 50.0, 25.0, 0.1)
    trihalomethanes = st.slider('Trihalomethanes', 0.0, 150.0, 75.0, 0.1)
    turbidity = st.slider('Turbidity', 0.0, 10.0, 5.0, 0.1)
    if st.button('Predict'):
        result = predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
        if result == 0:
            st.write('The water is not potable.')
        else:
            st.write('The water is potable.')

if __name__ == '__main__':
    main()

# Packages

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import ImageChops




# Load the trained model
with open("F:\project\Singapore_flat_resale_project\Resale_Flat_Prices.pkl" , "rb") as f:
    model = pickle.load(f)

# Define the Streamlit app
def main():
    st.title("HDB Resale Flat Price Prediction")
    st.write("Enter the details of the flat to predict its resale price.")

    # User inputs
    town = st.selectbox("Town", ['Ang Mo Kio', 'Bedok', 'Bishan', 'Bukit Batok', 'Bukit Merah', 'Bukit Panjang', 'Bukit Timah', 'Central Area', 'Choa Chu Kang', 'Clementi', 'Geylang', 'Hougang', 'Jurong East', 'Jurong West', 'Kallang/Whampoa', 'Marine Parade', 'Pasir Ris', 'Punggol', 'Queenstown', 'Sembawang', 'Sengkang', 'Serangoon', 'Tampines', 'Toa Payoh', 'Woodlands', 'Yishun'])
    flat_type = st.selectbox("Flat Type", ['1 Room', '2 Room', '3 Room', '4 Room', '5 Room', 'Executive', 'Multi-Generation'])
    flat_model = st.selectbox("Flat Model", ['Model A', 'Model B', 'Model C', 'Improved', 'New Generation', 'Simplified', 'Standard'])
    floor_area_sqm = st.number_input("Floor Area (sqm)", min_value=10, max_value=200, step=1)
    storey_start = st.number_input("Storey Start", min_value=1, max_value=50, step=1)
    storey_end = st.number_input("Storey End", min_value=1, max_value=50, step=1)
    remaining_lease_year = st.number_input("Remaining Lease (Years)", min_value=1, max_value=99, step=1)
    remaining_lease_month = st.number_input("Remaining Lease (Months)", min_value=0, max_value=11, step=1)
    lease_commence_date = st.date_input("Lease Commence Date")

    # Process input data
    input_data = pd.DataFrame({
        'town': [town],
        'flat_type': [flat_type],
        'flat_model': [flat_model],
        'floor_area_sqm': [floor_area_sqm],
        'storey_start': [storey_start],
        'storey_end': [storey_end],
        'remaining_lease_year': [remaining_lease_year],
        'remaining_lease_month': [remaining_lease_month],
        'lease_commence_date': [lease_commence_date.year]
    })


    # Predict resale price
    if st.button("Predict Resale Price"):
        prediction = model.predict(input_data)[0]
        st.success(f"The predicted resale price is: ${prediction:,.2f}")

# Run the app
if __name__ == '__main__':
    main()

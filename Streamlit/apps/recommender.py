import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

def app():
    # Title of the app
    st.title("Food Recommender System")

    # User input section
    st.sidebar.header("User Information")

    # Get user's age using a text input box
    age = st.sidebar.text_input("Enter Your Age", "25")

    # Convert the age input to an integer
    age = int(age) if age.isdigit() else 25

    # Get user's gender
    gender = st.sidebar.selectbox("Select Your Gender", ["Male", "Female"])

    # Get user's weight
    weight = st.sidebar.number_input("Enter Your Weight (kg)", min_value=1, max_value=500, value=70)

    # Get user's height
    height = st.sidebar.number_input("Enter Your Height (cm)", min_value=1, max_value=300, value=170)

    # Dropdown menu for activity level
    activity_options = ["Sedentary: little or no exercise", 
                        "Light: exercise 1-3 times/week", 
                        "Moderate: exercise 4-5 times/week", 
                        "Active: daily exercise or intense exercise 3-4 times/week", 
                        "Very Active: intense exercise 6-7 times/week", 
                        "Extra Active: very intense exercise daily, or physical job"]

    activity_level = st.sidebar.selectbox("Select Your Activity Level", activity_options)

    # Collects user input features into dataframe, set other features to default values
    data = {
            'Gender': gender,
            'Age': age,
            'Height': height/100,
            'Weight': weight,
            'family_history_with_overweight': 1.0,
            'FAVC': 1.0,
            'FCVC': 2.0,
            'NCP': 2.5, 
            'CAEC': 2.0,
            'SMOKE': 0.0,
            'CH2O': 2.0,
            'SCC': 0.0,
            'FAF': activity_options,
            'TUE': 1.0,
            'CALC': 2.0,
            'MTRANS': 3.0
    }
    input_df = pd.DataFrame(data)


    # Encoding of ordinal features
    input_df['Gender'] = input_df['Gender'].replace({
    'Female': 0.0,
    'Male': 1.0
    })

    input_df['FAF'] = input_df['FAF'].replace({
        'Sedentary: little or no exercise': 0.0,
        'Light: exercise 1-3 times/week': 0.6,
        "Moderate: exercise 4-5 times/week": 1.2, 
        "Active: daily exercise or intense exercise 3-4 times/week": 1.8, 
        "Very Active: intense exercise 6-7 times/week": 2.4, 
        "Extra Active: very intense exercise daily, or physical job": 3.0
    })

    # Display BMI
    BMI = weight/(height**2)*10000
    BMI = round(BMI, 1)
    st.write(f"Your BMI is {BMI} kg/m\u00B2.")

    # Button to trigger recommendations
    if st.sidebar.button("Get Food Recommendations"):
        # Display loading spinner while the recommender system is processing
        with st.spinner("Generating Recommendations..."):
            # Simulate a delay to mimic the time taken by the recommender system
            time.sleep(3)  # Replace this with the actual time your system takes


            # Reads in saved classification model
            load_clf = pickle.load(open('apps\Models\obesity_clf.pkl', 'rb'))
            

            # TODO Replace the following placeholder code with the actual call
            recommendations = ["Placeholder Recommendation 1", "Placeholder Recommendation 2", "Placeholder Recommendation 3"]


            # Placeholder for obesity level (replace with actual logic)
            # Apply model to make predictions
            obesity_num = load_clf.predict(input_df)[0]
            levels_in_order = ['Insufficient_Weight', 'Normal_Weight', 'Obesity_Type_I','Obesity_Type_II','Obesity_Type_III','Overweight_Level_I','Overweight_Level_II']
            obesity_level=levels_in_order[obesity_num]

        # Display recommendations once the loading is complete
        st.subheader("Food Recommendations")
        for i, recommendation in enumerate(recommendations, 1):
            st.write(f"{i}. {recommendation}")

        # Display user's obesity level
        st.subheader("Your Obesity Level")
        st.write(f"Based on the information provided, your obesity level is: {obesity_level}")

    # Display some information or instructions
    st.info("Enter your details on the left sidebar and click 'Get Food Recommendations' to see personalized suggestions-BY YOURS TRUELY BEN NGUYEN")
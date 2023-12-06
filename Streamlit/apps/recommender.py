import streamlit as st
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

    # Button to trigger recommendations
    if st.sidebar.button("Get Food Recommendations"):
        # Display loading spinner while the recommender system is processing
        with st.spinner("Generating Recommendations..."):
            # Simulate a delay to mimic the time taken by the recommender system
            time.sleep(3)  # Replace this with the actual time your system takes

            # TODO: Call your recommender system here with the user inputs
            # Replace the following placeholder code with the actual call
            recommendations = ["Placeholder Recommendation 1", "Placeholder Recommendation 2", "Placeholder Recommendation 3"]
            # Placeholder for obesity level (replace with actual logic)
            obesity_level = "Type I obesity"

        # Display recommendations once the loading is complete
        st.subheader("Food Recommendations")
        for i, recommendation in enumerate(recommendations, 1):
            st.write(f"{i}. {recommendation}")

        # Display user's obesity level
        st.subheader("Your Obesity Level")
        st.write(f"Based on the information provided, your obesity level is: {obesity_level}")

    # Display some information or instructions
    st.info("Enter your details on the left sidebar and click 'Get Food Recommendations' to see personalized suggestions-BY YOURS TRUELY BEN NGUYEN")
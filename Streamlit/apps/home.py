import streamlit as st

def app():
    st.title('Homepage')
    st.write('This is the `home page` of this project.')
    st.write('In this app, we will...')
    # Context Section
    # Deriving Insights
    st.header("Deriving Insights")
    st.write(
        "We aim to uncover significant correlations and patterns within the dataset, focusing particularly on understanding how lifestyle factors contribute to different weight classifications. By analyzing attributes such as family history, dietary habits, physical activity, and more, we seek to identify key determinants influencing weight outcomes."
    )
    
    # Food Recommendation System
    st.header("Food Recommendation System")
    st.write(
        "In addition to insights, we've developed a food recommendation system integrated into this analysis. The system takes into account your Age, Weight, Height, and Gender to generate personalized meal plans. It leverages the dataset to recommend balanced and nutritious meals tailored to individual health characteristics."
    )

    st.header("Dataset Context")
    
    st.write(
        "For this analysis, I utilized a dataset sourced from UC Irvine’s Machine Learning Repository, encompassing information on 2111 individuals aged 14 to 61. The dataset comprises 17 attributes, each offering unique insights into the respondents' lifestyles and health characteristics. Here's a brief overview of these attributes:"
    )
    
    # Attribute Descriptions
    attribute_descriptions = {
        "Gender": "Categorical - Female or Male",
        "Age": "Numeric - Age of the individual",
        "Height": "Numeric - Height in meters",
        "Weight": "Numeric - Weight in kilograms",
        "Family History": "Binary - Family history of obesity (Yes or No)",
        "FCHCF": "Binary - Frequent consumption of high caloric food (Yes or No)",
        "FCV": "Categorical - Frequency of vegetable consumption (1 = Never, 2 = Sometimes, 3 = Always)",
        "NMM": "Categorical - Number of main meals (1, 2, 3, or 4)",
        "CFBM": "Categorical - Consumption of food between meals (1 = No, 2 = Sometimes, 3 = Frequently, 4 = Always)",
        "Smoke": "Binary - Smoking habit (Yes or No)",
        "CW": "Categorical - Consumption of water (1 = Less than a liter, 2 = 1–2 liters, 3 = More than 2 liters)",
        "CCM": "Binary - Calorie consumption monitoring (Yes or No)",
        "PAF": "Categorical - Physical activity frequency per week (0 = None, 1 = 1 to 2 days, 2 = 2 to 4 days, 3 = 4 to 5 days)",
        "TUT": "Categorical - Time using technology devices a day (0 = 0–2 hours, 1 = 3–5 hours, 2 = More than 5 hours)",
        "CA": "Categorical - Consumption of alcohol (1 = Never, 2 = Sometimes, 3 = Frequently, 4 = Always)",
        "Transportation": "Categorical - Mode of transportation (Automobile, Motorbike, Bike, Public Transportation, Walking)",
        "Obesity": "Categorical - Weight classification (Insufficient weight, Normal weight, Level I overweight, Level II overweight, Type I obesity, Type II obesity, Type III obesity)"
    }
    
    # Display Attribute Descriptions
    for attribute, description in attribute_descriptions.items():
        st.write(f"- **{attribute}:** {description}")
    
    # Additional Information
    st.write(
        "The respondents in the dataset hail from Mexico, Peru, and Colombia, offering a diverse representation of lifestyles and cultural factors. The primary objective is to extract meaningful insights related to weight classification and lifestyle habits, fostering a deeper understanding of the interplay between health and daily routines."
    )
    

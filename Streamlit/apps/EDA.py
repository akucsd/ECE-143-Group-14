import streamlit as st
from PIL import Image  # Import Image from PIL


def app():
    st.title('Exploratory Data Analysis')
    
    st.image(
        Image.open("Images/Age.png"),
        caption="Age distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("Images/Genders.png"),
        caption="Age distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("Images/Height.png"),
        caption="Age distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("Images/Weight.png"),
        caption="Age distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("Images/Obesity.png"),
        caption="Age distribution",
        use_column_width=True,  # Adjust the width as needed
    )
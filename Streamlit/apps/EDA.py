import streamlit as st
from PIL import Image  # Import Image from PIL


def app():
    st.title('Exploratory Data Analysis')
    
    st.image(
        Image.open("apps\Images\Age.png"),
        caption="Age distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("apps\Images\Genders.png"),
        caption="Gender distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("apps\Images\Height.png"),
        caption="Height distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("apps\Images\Weight.png"),
        caption="Weight distribution",
        use_column_width=True,  # Adjust the width as needed
    )
    st.image(
        Image.open("apps\Images\Obesity.png"),
        caption="Obesity distribution",
        use_column_width=True,  # Adjust the width as needed
    )
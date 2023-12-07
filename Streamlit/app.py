import streamlit as st
from multiapp import MultiApp
from apps import home, recommender, EDA

app = MultiApp()
st.markdown("""
# ECE 143 Group 14
Please select...
""")

app.add_app('Homepage', home.app)
app.add_app('Exploratory Data Analysis', EDA.app)
app.add_app('Recommender', recommender.app)

app.run()
import streamlit as st
from multiapp import MultiApp
from apps import home, data, model

app = MultiApp()
st.markdown("""
# ECE 143 Group 14
Please select...
""")

app.add_app('Home', home.app)
app.add_app('Data', data.app)
app.add_app('Model', model.app)

app.run()
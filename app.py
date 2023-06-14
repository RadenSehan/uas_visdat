import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

DATA_URL = (
    "Esport data.xlsx"
)

st.title("Esports Earnings")
st.markdown("Esports (olahraga elektronik) adalah bentuk kompetisi olahraga yang menggunakan video game. Esports sering kali berbentuk kompetisi video game multipemain yang terorganisir, terutama antara pemain profesional, baik secara individu maupun tim.")
image = Image.open('esport.png')
st.image(image, use_column_width = True)

#sidebar
st.sidebar.markdown("## Side Panel")
st.sidebar.markdown("Use this panel to explore the dataset and create own viz.")


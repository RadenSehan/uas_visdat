import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

tab1, tab2 = st.tabs(["🗒️ About","📈 Chart"])
df = pd.read_excel(
    "Esport data.xlsx"
)

#tab1
tab1.title("Esports Earnings")
image = Image.open('esport.png')
tab1.image(image, use_column_width = True)
tab1.markdown("Esports (olahraga elektronik) adalah bentuk kompetisi olahraga yang menggunakan video game. Esports sering kali berbentuk kompetisi video game multipemain yang terorganisir, terutama antara pemain profesional, baik secara individu maupun tim.")

#sidebar
st.sidebar.markdown("## Filter Column")

#tab2
view_all = st.sidebar.checkbox("View all data")
tab2.title("Data Earnings Esports")
genre_filter = st.sidebar.selectbox("Filter by Genre", options=df['Genre'].unique())

if view_all:
    tab2.dataframe(df)

filter_data = df[
    (df['Genre'] == genre_filter)
]
if not view_all:
    tab2.dataframe(filter_data)

tab2.write("Bar Chart:")
tab2.bar_chart(filter_data, x="Game", y="TotalPlayers")
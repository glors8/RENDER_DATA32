#cargar librerías
import pandas as pd
import numpy as np

import plotly.express as px
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/jsaraujott/datos/refs/heads/main/iris.csv")
df["type"] = df["type"].astype("str")

#Titulo a nuestro reporte
st.header("Relación de variables", divider = "gray")
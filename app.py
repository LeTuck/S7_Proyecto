import streamlit as st
import pandas as pd
import plotly.express as px
import scipy.stats

st.header('Datos de Vehiculos')


st.title("Análisis de Datos de Autos")

fuel_types = list(car_data["FUEL"].unique())
selected_fuel = st.multiselect("Selecciona el tipo de combustible:", fuel_types, default=fuel_types)

filtered_data = car_data[car_data["FUEL"].isin(selected_fuel)]

st.subheader("Distribución de Precios de Autos")
fig = px.histogram(filtered_data, x="PRICE", nbins=30, marginal="box", title="Distribución de Precios")
st.plotly_chart(fig)

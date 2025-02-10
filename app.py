import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv("../vehicles_us.csv")

# Crear la interfaz de la aplicación
st.title("Cuadro de Mandos de Vehículos")
st.header("Análisis de Datos de Vehículos en Venta")

# Botón para mostrar histograma
if st.button("Mostrar Histograma de Precios"):
    fig = px.histogram(car_data, x="PRICE", title="Distribución de Precios de Vehículos")
    st.plotly_chart(fig)

import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar los datos
car_data = pd.read_csv("vehicles_us.csv")

# Limpiar Datos
car_data['model_year'] = car_data['model_year'].fillna(car_data['model_year'].mean()).astype(int)
car_data['model'] = car_data['model'].str.upper()
car_data['condition'] = car_data['condition'].str.upper().fillna('UNKNOWN').astype('category')
car_data['cylinders'] = car_data['cylinders'].fillna(car_data['cylinders'].mean()).astype(int)
car_data['fuel'] = car_data['fuel'].str.upper().astype('category')
car_data['odometer'] = car_data['odometer'].fillna('0').astype('int')
car_data['transmission'] = car_data['transmission'].str.upper()
car_data['type'] = car_data['type'].str.upper()
car_data['paint_color'] = car_data['paint_color'].str.upper().fillna('UNKNOWN').astype('category')
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])
car_data['is_4wd'] = car_data['is_4wd'].fillna('0').astype('int')
car_data.columns = car_data.columns.str.upper()

# Crear la interfaz de la aplicación
st.title("Cuadro de Mandos de Vehículos")
st.header("Análisis de Datos de Vehículos en Venta")
st.header("Base de Datos:")
st.write(car_data)

# Botón para mostrar histograma de precios
if st.button("Mostrar Histograma de Precios"):
    fig = px.histogram(car_data, x="PRICE", title="Distribución de Precios de Vehículos")
    st.plotly_chart(fig)
    
st.write("Tabla de dispersión entre las variables numéricas:")

# Seleccionar columnas numéricas para la tabla de dispersión
numeric_columns = car_data.select_dtypes(include='number').columns.tolist()

# Crear un gráfico de dispersión usando plotly_express
scatter_matrix = px.scatter_matrix(car_data, dimensions=numeric_columns, title="Matriz de Dispersión")
st.plotly_chart(scatter_matrix)    

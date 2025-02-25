import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

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

st.title("Venta de Vehículos")
st.header("Escoge el tipo de grafica")

if st.button('Condicion de vehiculos'):
    long_format_data = car_data.groupby(['CONDITION', 'TYPE']).size().reset_index(name='Numero de Vehiculos')
    
    fig = px.bar(long_format_data, x='CONDITION', y='Numero de Vehiculos', color='TYPE', 
                 title="Condicion de los vehiculos")
    st.plotly_chart(fig)
    
if st.button('Modelo y Precio'):
    long_format_data = car_data.groupby(['PRICE', 'MODEL']).size().reset_index(name='Numero de Vehiculos')
    
    fig = px.bar(long_format_data, x='PRICE', y='Numero de Vehiculos', color='MODEL', 
                 title="Modelo y Precio")
    st.plotly_chart(fig)

st.header("Fuente de Datos:")
st.write(car_data)
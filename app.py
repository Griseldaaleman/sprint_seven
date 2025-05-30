import streamlit as st
import pandas as pd
import plotly.express as px

#Cargo el dataset
df = pd.read_csv("vehicles_us.csv")

#Añado el header de la aplicación
st.header("Análisis de anuncios de autos en EE.UU")

#Muestro los primeros datos del dataset
st.write('Primeros registros del dataset:')
st.write(df.head())

#Creo el boton para histograma
if st.button('Mostrar histograma de precios:'):
    fig = px.histogram(df, x='price', title='Distribución de Precios de Autos')
    st.plotly_chart(fig)

#Creo un boton para grafico de dispersión
if st.button('Mostrar gráfico de dispersión (odómetro vs precio)'):
    fig = px.scatter(df, x='odometer', y='price', color='type', title='Precio vs Kilometraje')
    st.plotly_chart(fig)

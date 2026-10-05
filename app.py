import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo os dados
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho do aplicativo
st.header('Painel de Anúncios de Venda de Carros')

# Botão para o histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma da quilometragem (odometer) dos veículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botão para o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: quilometragem x preço')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

    
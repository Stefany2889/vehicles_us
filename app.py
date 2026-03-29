import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv(
    'vehicles_us.csv')  # leer los datos


st.set_page_config(
    page_title="Vehiculos de EUA",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)


st.header(
    " :blue[Características de los veículos de EUA]", divider="gray")
"""
    :material/traffic_jam: Algunas estadísiticas importantes.
    """


st.write('Selecciona el tipo de gráfico que deseas ver:')

check_histograma = st.checkbox("Histograma")
check_dispercion = st.checkbox("Gráfica de disperción")


if check_histograma:

     st.write(
            'Selecciona cual histograma deseas generar:')


    check_precio = st.checkbox("Histograma de la variable precio")
    check_odometer = st.checkbox("Histograma de la variable odometer")
    check_año = st.checkbox("Histograma de la variable model_year")

    if check_precio:
        st.write(
            'Creación de un histograma para el conjunto de datos de los precios para autos en EUA')

        # crear un histograma
        fig = px.histogram(car_data, x="price")

        st.plotly_chart(fig, use_container_width=True)

    if check_odometer:
        st.write(
            'Creación de un histograma para el conjunto de datos del odometro para autos en EUA')

        # crear un histograma
        fig = px.histogram(car_data, x="odometer")

        st.plotly_chart(fig, use_container_width=True)

    if check_año:
        st.write(
            'Creación de un histograma para el conjunto de datos del año del modelo para autos en EUA')

        # crear un histograma
        fig = px.histogram(car_data, x="model_year")

        st.plotly_chart(fig, use_container_width=True)


if check_dispercion:

    st.write(
        'Creación de un gráfico de disperción para el conjunto de datos de anuncios de venta de coches')

    # crear un scatter plot
    fig = px.scatter(car_data, x="model_year", y="price")

    st.plotly_chart(fig, use_container_width=True)

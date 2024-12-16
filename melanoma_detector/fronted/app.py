import streamlit as st
from PIL import Image
import requests
import json
import os

url="http://localhost:8000"

# Configuración inicial de la página de Streamlit
st.set_page_config(
    page_title="Detector de melanoma",
    page_icon='🖼️',
    layout="wide",
    initial_sidebar_state="expanded",
)

# Título y descripción de la aplicación
st.header('Detector de melanoma 📸')
st.markdown('''
    Esta aplicación utiliza un modelo de Deep Learning para analizar imágenes y determinar si existe riesgo de melanoma.

    *Nivel de riesgo:*
    - [Alto]: Probabilidad significativa de melanoma.
    - [Bajo]: Riesgo bajo, pero consulte a un dermatólogo si tiene dudas.
''')
st.markdown("---")

# Crear la entrada para cargar una imagen
st.markdown("### Suba una imagen para su análisis 👇")
new_input = st.file_uploader("Cargar imagen", type=['jpg', 'jpeg', 'png'])

if new_input is not None:
    col1, col2 = st.columns(2)

    with col1:
        # Mostrar la imagen cargada por el usuario
        st.image(Image.open(new_input), caption="Imagen cargada ☝️", width=250)
        img_bytes=new_input.getvalue()

    with col2:
        # Botón para analizar la imagen
        st.button("Analizar imagen")
        st.spinner("Analizando la imagen, por favor espere...")
        # Realizar solicitud a la API
        res=requests.post(url+"/predict",files={"img":img_bytes})

        if res.status_code==200:
            st.success("File processed succesfully! ✅")
            response = res.json()
            risk = response.get("fare")

            if risk:
                st.markdown(f"Resultado: ##{risk}##")
            else:
                st.error("No se pudo determinar el nivel de riesgo. Por favor, intente de nuevo.")

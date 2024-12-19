import streamlit as st
from PIL import Image
import requests
import json
import os

url="http://localhost:8000"

# Configuración inicial de la página de Streamlit
st.set_page_config(
    page_title="Detector de Melanoma",
    page_icon='🖼️',
    layout="centered",
    initial_sidebar_state="expanded",
)
# 📸
# Título y descripción de la aplicación
st.title('Detector de Melanoma :material/add_a_photo: :material/health_metrics:')
st.markdown('''
    Esta interfaz utiliza un modelo avanzado de Deep Learning que permite analizar imágenes de lesiones de piel estimando una probabilidad de que pueda ser melanoma.

    Su propósito es servir como un apoyo preventivo en la detección temprana, ayudándote a tomar decisiones informadas sobre tu salud.
''')
st.subheader("¿Cómo funciona?")
st.markdown('''
    - PASO :one:: Sube una imagen clara de la zona que deseas evaluar.
    - PASO :two:: Nuestro modelo analizará la imagen.
    - PASO :three:: Recibirás un porcentaje de probabilidad junto con una orientación sobre posibles próximos pasos.
''')

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    # Crear la entrada para cargar una imagen
    st.markdown("#### :one: Suba una imagen para su análisis :material/upload_2: :material/image_search:")
    new_input = st.file_uploader("Cargar imagen", type=['jpg', 'jpeg', 'png'])

    if new_input is not None:
        # Mostrar la imagen cargada por el usuario
        st.image(Image.open(new_input), caption="Imagen cargada ☝️", width=250)
        img_bytes = new_input.getvalue()


with col2:
    # Botón para analizar la imagen
    st.markdown("#### :two: Presiona el Botón para análisis :material/web_traffic:")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    if st.button("Analizar imagen"):
        with st.spinner("Analizando la imagen, por favor espere..."):
    # Realizar solicitud a la API
            res=requests.post(url+"/predict",files={"img":img_bytes})

            if res.status_code==200:
                st.success("File processed succesfully! ✅")
                response = res.json()
                risk = response.get("fare")
                risk_format = "{:.2%}".format(risk)

        #if risk:
                st.markdown(f":three: __Probabilidad de Melanoma: {risk_format}__")

                if risk <= 0.20:
                    st.success("Monitoreo Recomendado: Recomendamos hacer seguimiento regular de su piel y en caso de dudas consultar a un Dermatólogo.")
                elif 0.21 <= risk <= 0.49:
                    st.warning(" Revisión Sugerida: Recomendamos hacer seguimiento regular de su piel y considerar una visita a un Dermatólogo")
                elif risk >=0.50:
                    st.error("Consulta Recomendada: Recomendamos una revisión médica con Dermatólogo para mayor tranquilidad.")
                else:
                    st.error("No se pudo determinar el nivel de riesgo. Por favor, intente de nuevo.")



            else:
                st.error("Error en la solicitud a la API. Por favor, intente más tarde.")

st.divider()
st.info("Recuerda que esta evaluación es una herramienta de apoyo y en ningún caso puede utilizarse como un diagnóstico médico. Si tienes dudas, un dermatólogo 🧑‍⚕️:material/stethoscope: es la mejor fuente de información.")

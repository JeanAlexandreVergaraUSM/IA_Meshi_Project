import streamlit as st
import requests
import base64
import os
from googletrans import Translator

translator = Translator()

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string.decode()}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

fondo_path = os.path.join(base_dir, 'Fondo.jpg')
add_bg_from_local(fondo_path)

st.markdown("<h1 style='color:white;'>IA Meshi - Generador de Recetas en Tiempo Real</h1>", unsafe_allow_html=True)

st.markdown("<iframe src='http://localhost:8001/video_feed' width='900' height='600'></iframe>", unsafe_allow_html=True)

if st.button("Capturar y Reconocer Alimento"):
    response = requests.get("http://localhost:8001/capture_frame")
    
    if response.status_code == 200:
        st.markdown("<p style='color:black;'>Reconociendo su alimento. Por favor espere...</p>", unsafe_allow_html=True)
        recipe_response = requests.post("http://localhost:8000/generate_recipe/")
        
        if recipe_response.status_code == 200:
            data = recipe_response.json()
            
            title = data.get('Título', 'Título no disponible')
            recipe = data.get('Receta', 'Receta no disponible')
            food_item = data.get('food_item', 'Alimento no detectado')
            
            translated_food_item = translator.translate(food_item, dest='es').text
            
            st.markdown(f"<p style='color:black;'>Alimento detectado: {translated_food_item}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black;'>Título de la receta: {title}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:black;'>{recipe}</p>", unsafe_allow_html=True)
        else:
            st.error("Error al intentar generar la receta.")
    else:
        st.error("No se pudo capturar la imagen.")

from fastapi import FastAPI
import torch
from PIL import Image
import os
from transfer_learning_model import predict_food_item
from recipe_generator import generate_recipe_from_ingredient

app = FastAPI()

# Obtener la ruta de la carpeta actual (IA_Meshi_Project)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Crear la carpeta Images/Capturas dentro de IA_Meshi_Project
output_folder = os.path.join(base_dir, "Images", "Capturas")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Crear la carpeta si no existe

image_path = os.path.join(output_folder, "captured_frame.jpg")

@app.post("/generate_recipe/")
async def generate_recipe():
    if os.path.exists(image_path):
        img = Image.open(image_path)
        detected_food = predict_food_item(image_path)
        
        if detected_food:
            recipe = generate_recipe_from_ingredient(detected_food)
            return {
                "food_item": detected_food,
                "Título": recipe['Título'],
                "Receta": recipe['Receta']
            }
        else:
            return {"error": "No se detectó ningún alimento en la imagen capturada"}
    else:
        return {"error": f"No se encontró la imagen capturada en {image_path}"}

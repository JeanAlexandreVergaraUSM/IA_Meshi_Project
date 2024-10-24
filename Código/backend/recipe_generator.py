import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from googletrans import Translator

# Cargar el modelo GPT-2 preentrenado y su tokenizador
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Asegurarse de que el token de padding sea el mismo que el token de finalización
tokenizer.pad_token = tokenizer.eos_token

# Inicializar el traductor
translator = Translator()

# Función para generar una receta a partir del nombre del alimento detectado
def generate_recipe_from_ingredient(food_item):
    # Crear un prompt más directo
    prompt = f"Ingredientes para {food_item}:"

    # Tokenizar la entrada
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generar texto utilizando el modelo GPT-2
    outputs = model.generate(
        inputs,
        max_length=200,  # Ajustar la longitud máxima de la receta
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    
    # Decodificar la salida generada
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Limpiar el texto para que contenga solo ingredientes y pasos
    recipe_clean = limpiar_receta(recipe)

    # Traducir la receta al español
    translated_recipe = translate_to_spanish(recipe_clean)
    
    # Generar el título de la receta
    title = f"Receta de {food_item.capitalize()}"
    
    return {'Título': title, 'Receta': translated_recipe}

# Función para limpiar la receta eliminando detalles irrelevantes
def limpiar_receta(recipe_text):
    # Mantener solo la parte de ingredientes y pasos
    start = recipe_text.find("Ingredientes:")
    if start == -1:
        return recipe_text  # Si no encuentra "Ingredientes:", devuelve el texto tal cual
    return recipe_text[start:]

# Función de traducción usando googletrans
def translate_to_spanish(text):
    try:
        translated = translator.translate(text, dest='es')
        return translated.text
    except Exception as e:
        return f"Error en la traducción: {e}"

import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from googletrans import Translator

model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

tokenizer.pad_token = tokenizer.eos_token

translator = Translator()

def generate_recipe_from_ingredient(food_item):
    prompt = f"Ingredientes para {food_item}:"

    inputs = tokenizer.encode(prompt, return_tensors='pt')
    
    outputs = model.generate(
        inputs,
        max_length=200,  
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )
    
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    recipe_clean = limpiar_receta(recipe)

    translated_recipe = translate_to_spanish(recipe_clean)
    
    title = f"Receta de {food_item.capitalize()}"
    
    return {'Título': title, 'Receta': translated_recipe}

def limpiar_receta(recipe_text):
    start = recipe_text.find("Ingredientes:")
    if start == -1:
        return recipe_text  
    return recipe_text[start:]

def translate_to_spanish(text):
    try:
        translated = translator.translate(text, dest='es')
        return translated.text
    except Exception as e:
        return f"Error en la traducción: {e}"

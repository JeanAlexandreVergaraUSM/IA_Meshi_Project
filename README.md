# IA Meshi - Generador de Recetas en Tiempo Real

Este proyecto utiliza una IA para reconocer alimentos capturados por una cámara en tiempo real y generar recetas basadas en el alimento detectado. Se compone de un **backend** que realiza la detección del alimento y la generación de recetas, y un **frontend** que muestra los resultados en una interfaz web. 

## Estructura del Proyecto

```IA_Meshi_Project/ 
└── backend/ │ ├── pycache/ │ ├── camera_capture.py │ ├── main.py │ ├── recipe_generator.py │ ├── transfer_learning_model.py │ 
└── Entreno/ │ ├── best_model4.pth │ ├── best_model4.txt │ ├── best_model6.pth │ ├── best_model6.txt │ 
└── frontend/ │ ├── app.py │ ├── camera_stream.py │ 
└── Fondo.jpg
```


## Requisitos Previos

Para ejecutar este proyecto, necesitarás tener instalado:

- **Python 3.8+**
```
sudo apt install python3.8 python3.8-venv python3.8-dev
```
  
- **FastAPI**
```
pip install fastapi
```
- **Uvicorn**
```
pip install uvicorn
```
- **Streamlit**
```
pip install streamlit
``` 
- **Torch**
```
pip install torch torchvision
```
- **Transformers (Hugging Face)**
```
pip install transformers
```
- **OpenCV**
```
pip install opencv-python
```
- **Googletrans**
```
pip install googletrans==4.0.0rc1
```

## Configuración del Proyecto

1.Clona este repositorio:
```
git clone https://github.com/JeanAlexandreVergaraUSM/IA_Meshi_Project.git
```
```
cd IA_Meshi_Project
```
2.Crea un entorno virtual:
```
python3 -m venv myenv
source myenv/bin/activate  # Activar entorno virtual en Linux
```

## Ejecución del Backend

1.Navega a la carpeta backend:
```
cd backend
```
2.Ejecuta el servidor de FastAPI utilizando uvicorn:
```
uvicorn main:app --reload
```
## Ejecución del Frontend

1.Navega a la carpeta frontend:
```
cd frontend
```
2.Ejecuta la aplicación de Streamlit:
```
streamlit run app.py
```
## Funcionamiento del Proyecto

# Backend
El backend utiliza FastAPI para servir dos rutas principales:
POST /generate_recipe/: Recibe la imagen capturada, predice el alimento utilizando modelos preentrenados, y genera una receta usando GPT-2.

### Frontend
El frontend está basado en Streamlit y muestra el video en vivo de la cámara. Al presionar un botón, captura la imagen, llama al backend para predecir el alimento y muestra la receta generada.

### Modelos
Los modelos utilizados están basados en ResNet18 entrenados previamente para identificar varios alimentos. Los archivos .pth contienen los pesos de los modelos y están ubicados en la carpeta Entreno.

### Estructura del Código

## Archivos Importantes:
```
-backend/main.py: Punto de entrada del backend. Inicia FastAPI y expone las rutas necesarias para generar recetas.
-backend/transfer_learning_model.py: Carga los modelos entrenados para identificar alimentos.
-backend/recipe_generator.py: Genera recetas a partir de los alimentos detectados utilizando GPT-2.
-frontend/app.py: Contiene la lógica de la interfaz de usuario con Streamlit.
-frontend/camera_stream.py: Muestra el video en vivo y captura imágenes desde la cámara utilizando Flask y OpenCV.
```
## Datos Personales

### Estudiantes:
```
1) Fernando Zamora
-Rol: 202230541-k

2) Lorenzo Gonzalez
-Rol: 202230550-9

3) Jean Alexandre
-Rol: 202230562-2
```





import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os

# Transformations for the image
data_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Obtener la ruta base (IA_Meshi_Project)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Función para cargar cada modelo entrenado con su número de clases correspondiente
def load_model(model_path, num_classes):
    model = models.resnet18(pretrained=False)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()  # Poner el modelo en modo de evaluación
    return model

# Cargar los modelos con sus archivos .pth correspondientes
models = [
    load_model(os.path.join(base_dir, 'Entreno', 'best_model4.pth'), 19),
    load_model(os.path.join(base_dir, 'Entreno', 'best_model6.pth'), 15)
]

# Listas de clases correspondientes a cada modelo
class_lists = [
    os.path.join(base_dir, 'Entreno', 'best_model4.txt'),
    os.path.join(base_dir, 'Entreno', 'best_model6.txt')
]

# Función combinada para predecir el alimento utilizando los modelos
def predict_food_item(image_path):
    image = Image.open(image_path)
    image = data_transforms(image).unsqueeze(0)

    predictions = []
    for i, model in enumerate(models):
        with torch.no_grad():
            output = model(image)
            _, pred = torch.max(output, 1)
            predictions.append(pred.item())

    predicted_classes = []
    for i, class_list in enumerate(class_lists):
        with open(class_list, 'r') as f:
            classes = f.read().splitlines()
        predicted_classes.append(classes[predictions[i]])

    # Votación mayoritaria entre las predicciones de los modelos
    final_prediction = max(set(predicted_classes), key=predicted_classes.count)
    return final_prediction

import cv2
import os

def capture_image(file_format="jpg"):
    capture_folder = "capturas"
    if not os.path.exists(capture_folder):
        os.makedirs(capture_folder)

    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise Exception("No se pudo abrir la cámara")

    ret, frame = cap.read()
    if not ret:
        raise Exception("No se pudo capturar la imagen")
    
    img_path = os.path.join(capture_folder, f"captured_frame.{file_format}")
    if file_format == "jpg":
        success = cv2.imwrite(img_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    elif file_format == "png":
        success = cv2.imwrite(img_path, frame, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

    if success:
        print(f"Imagen guardada en: {img_path}")
    else:
        raise Exception(f"No se pudo guardar la imagen en formato {file_format}")
    
    cap.release()
    return img_path

from flask import Flask, Response
import cv2
import os
import atexit

app = Flask(__name__)

base_dir = os.path.dirname(os.path.abspath(__file__))

output_folder = os.path.join(base_dir, "Images", "Capturas")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)  

def initialize_camera():
    cap = None
    i = 0
    while i < 10: 
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            break
        cap.release()
        i += 1
    else:
        print("Error: No se pudo acceder a ninguna cámara.")
        exit()

    return cap

cap = initialize_camera()

atexit.register(lambda: cap.release())

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/capture_frame')
def capture_frame():
    ret, frame = cap.read()
    if ret:
        output_path = os.path.join(output_folder, "captured_frame.jpg")
        success = cv2.imwrite(output_path, frame)
        if success:
            return "Frame capturado correctamente", 200 
        else:
            return "Error: No se pudo guardar el frame.", 500
    else:
        return "Error: No se pudo capturar el frame.", 500


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=False, use_reloader=False)

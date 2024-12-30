import base64
import cv2
import numpy as np
from flask import Flask, render_template, request, Response
from ultralytics import YOLO
import os
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  
socketio = SocketIO(app)


model = YOLO("runs/detect/train2/weights/best.pt")


camera = cv2.VideoCapture(0)

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Kameradan alınan görüntüleri işle
@app.route('/predict_camera', methods=['POST'])
def predict_camera():
  
    image_data = request.form['image']
    image_data = image_data.split(',')[1]  # Base64 header'ı kaldır
    image = np.frombuffer(base64.b64decode(image_data), np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

   
    results = model.predict(source=image)

   
    annotated_image = results[0].plot()
    output_path = os.path.join("static", "camera_result.jpg")
    cv2.imwrite(output_path, annotated_image)

    return render_template('result.html', input_image=output_path, output_image=output_path)

# Dosya yükleme ve tahmin
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "Dosya yüklenmedi!"
    
    file = request.files['file']
    if file.filename == '':
        return "Bir dosya seçin!"
   
    input_path = os.path.join("static", file.filename)
    file.save(input_path)
   
    image = cv2.imread(input_path)
    results = model.predict(source=image)
    
   
    annotated_image = results[0].plot()
    output_path = os.path.join("static", "result.jpg")
    cv2.imwrite(output_path, annotated_image)
    
    return render_template('result.html', input_image=input_path, output_image=output_path)

# Canlı video akışı
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        
       
        results = model.predict(source=frame, show=False)
        annotated_frame = results[0].plot()

       
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

   
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Canlı tespit sayfası
@app.route('/live')
def live():
    return render_template('live.html')

if __name__ == '__main__':
    app.run(debug=True)

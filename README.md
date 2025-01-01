YOLO-Based Pothole Detection System 

This project is a system for detecting potholes using a pre-trained YOLO model. The project provides a Flask-based web interface, allowing users to perform pothole detection through both file uploads and live camera streams. 

 

📊 Project Features 

Pothole Detection: Detects potholes in images or live camera streams. 

File Upload: Users can upload an image file to detect potholes. 

Live Camera Stream: Perform real-time pothole detection via the camera stream. 

Real-Time Predictions: Identify and localize potholes using the pre-trained YOLO model. 

 

📷 Project Screenshots 

Home Page 

Users can upload an image to perform pothole detection. 

<img width="948" alt="main_page" src="https://github.com/user-attachments/assets/a8f1c1f6-3265-4eae-b344-1901c1ae5e36" />

 <img width="960" alt="{B1B51710-7FC7-4FD5-8915-A2F8903EB9AC}" src="https://github.com/user-attachments/assets/20d56a88-fbc4-46fe-9e0b-5859b5ed27c3" />

 
 

🚀 Requirements 

Follow the steps below to run the project: 

Python Version 

Python 3.8 or higher. 

Required Libraries 

Install the dependencies using the following command: 

pip install -r requirements.txt 

Contents of requirements.txt: 

flask 
flask-socketio 
ultralytics 
opencv-python 
numpy 
eventlet 

 

🔧 Setup Instructions 

1. Clone the Repository 

Clone the GitHub repository to your local machine: 

git clone https://github.com/<your-username>/<repo-name>.git 
cd <repo-name> 

2. Create a Virtual Environment (Optional) 

Create an isolated environment to run the project: 

python3 -m venv myenv 
source myenv/bin/activate  # Windows: myenv\Scripts\activate 

3. Install Dependencies 

Install the required dependencies: 

pip install -r requirements.txt 

4. Start the Flask Server 

Run the project using: 

python app.py 

5. Open the Web Interface 

Visit the following address in your browser: 

http://127.0.0.1:5000/ 

 

📝 Project Structure 

clean-detect/ 
├── app.py                  # Main Flask application file 
├── camera.py               # Camera operations 
├── templates/              # HTML files 
│   ├── index.html 
│   ├── result.html 
│   ├── live.html 
├── static/                 # Static files (CSS, JS, images) 
│   ├── styles.css 
│   ├── script.js 
│   ├── images/ 
├── data.yaml               # YOLO data configuration file 
├── requirements.txt        # Required Python libraries 
└── README.md               # Project documentation 

 

🛠️ Usage 

Pothole Detection via File Upload 

Select an image file from the home page. 

Click the "Predict" button. 

View the detected potholes in the image. 

Real-Time Pothole Detection via Live Camera 

Navigate to the "Live Detection" page. 

Watch real-time pothole detections from your camera. 

 

📢 License 

This project is licensed under the MIT License. 

 

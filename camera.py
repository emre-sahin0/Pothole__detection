import cv2

cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Kamera açılamadı!")
else:
    print("Kamera başarıyla açıldı!")

cap.release()

from ultralytics import YOLO
import cv2


model = YOLO("runs/detect/train2/weights/best.pt")  


image_path = "test.png" 
image = cv2.imread(image_path)


results = model.predict(source=image, save=True, show=True)  


annotated_image = results[0].plot() 
cv2.imwrite("annotated_test.jpg", annotated_image)  

print("Tahmin tamamlandı. Annotated görüntü 'annotated_test.jpg' olarak kaydedildi.")

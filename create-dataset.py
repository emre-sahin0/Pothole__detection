import os
import shutil

source_folder = "/home/emre123/detect/Pothole-Detection"

image_target_folder = "data/images"
label_target_folder = "data/labels"


os.makedirs(image_target_folder, exist_ok=True)
os.makedirs(label_target_folder, exist_ok=True)


for file_name in os.listdir(source_folder):
    source_path = os.path.join(source_folder, file_name) 
    if file_name.endswith(".jpg") or file_name.endswith(".png"): 
        shutil.move(source_path, os.path.join(image_target_folder, file_name))
    elif file_name.endswith(".txt"): 
        shutil.move(source_path, os.path.join(label_target_folder, file_name))

print("Dosyalar başarıyla taşındı!")

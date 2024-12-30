import os
import shutil
import random

# Veri seti klasörlerini tanımlayın
image_folder = "data/images"
label_folder = "data/labels"
train_image_folder = "data/train/images"
train_label_folder = "data/train/labels"
test_image_folder = "data/test/images"
test_label_folder = "data/test/labels"

# Hedef klasörleri oluştur
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)
os.makedirs(test_image_folder, exist_ok=True)
os.makedirs(test_label_folder, exist_ok=True)

# Tüm görüntü dosyalarını al
image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]

# Dosyaları rastgele karıştır
random.shuffle(image_files)

# Eğitim ve test bölme oranını tanımlayın
split_ratio = 0.8
split_index = int(len(image_files) * split_ratio)

train_files = image_files[:split_index]
test_files = image_files[split_index:]

# Dosyaları taşımak için bir fonksiyon
def move_files(file_list, source_image_folder, source_label_folder, target_image_folder, target_label_folder):
    for file_name in file_list:
        base_name = os.path.splitext(file_name)[0]
        # Görüntü ve etiket dosyalarını taşı
        shutil.move(os.path.join(source_image_folder, file_name), os.path.join(target_image_folder, file_name))
        shutil.move(os.path.join(source_label_folder, base_name + ".txt"), os.path.join(target_label_folder, base_name + ".txt"))

# Eğitim dosyalarını taşı
move_files(train_files, image_folder, label_folder, train_image_folder, train_label_folder)

# Test dosyalarını taşı
move_files(test_files, image_folder, label_folder, test_image_folder, test_label_folder)

print("Veri seti başarıyla ayrıldı!")

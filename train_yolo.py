from ultralytics import YOLO

# YOLO modelini yükle (Nano model, hızlı ve hafif)
model = YOLO("yolo11n.pt")  # Nano model; daha büyük bir model için 'yolo11m.pt' veya 'yolo11l.pt' seçebilirsiniz.

# Modeli eğit
model.train(
    data="data.yaml",   # Veri seti konfigürasyon dosyası
    epochs=10,          # 10 epoch ile daha kısa sürede sonuç
    imgsz=320,          # Görüntü boyutunu 320 piksele düşürerek hız kazanır
    batch=8,            # Daha küçük batch boyutu ile bellek tasarrufu
    patience=5,         # Erken durdurma, ilerleme yoksa 5 epoch sonra durur
    device="0"          # GPU kullanımı için (CPU için 'cpu' yazabilirsiniz)
)

print("Eğitim tamamlandı! Model en iyi ağırlıkları kaydetti.")

# Configurația proiectului

Proiectul folosește fișiere `.yaml` sau `.json` pentru a seta:

## ⚙️ Setări model

- input size: [224, 224] 
- backbone: MobileNetV2
- learning_rate: 0.0001
- epochs: 20-50
- batch_size: 16 sau 32

## 📂 Setări directoare

- raw_dir: data/raw
- processed_dir: data/processed
- train_dir: data/train
- validation_dir: data/validation
- test_dir: data/test

## 🧪 Setări de augmentare

- flip
- rotate
- zoom
- shear

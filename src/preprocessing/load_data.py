import os
from pathlib import Path
from PIL import Image

def load_images_from_folder(folder):
    images = []
    labels = []
    for class_name in os.listdir(folder):
        class_path = Path(folder) / class_name
        if not class_path.is_dir():
            continue
        for img_file in class_path.iterdir():
            try:
                img = Image.open(img_file).convert("RGB")
                images.append(img)
                labels.append(class_name)
            except:
                print(f"Eroare la citirea imaginii: {img_file}")
    return images, labels


import os
from PIL import Image

def resize_images(root_folder, size=(640, 640)):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
                file_path = os.path.join(dirpath, filename)
                try:
                    img = Image.open(file_path)
                    img = img.resize(size, Image.LANCZOS)
                    img.save(file_path)
                    print(f"Redimensionat: {file_path}")
                except Exception as e:
                    print(f"Eroare la {file_path}: {e}")

if __name__ == "__main__":
    folder = r"A:\cats_dogs_light\Proiect RN COMARDICI ALEXANDRU\dataset\train"
    resize_images(folder)

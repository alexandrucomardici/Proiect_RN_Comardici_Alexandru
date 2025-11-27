import os
import shutil
import random

def split_images(source_folder, output_folder, train_ratio=0.8, val_ratio=0.2):
    # Folderele finale
    train_folder = os.path.join(output_folder, "train")
    validation_folder = os.path.join(output_folder, "validation")
    test_folder = os.path.join(output_folder, "test")

    # Creăm folderele dacă nu există
    for folder in [train_folder, validation_folder, test_folder]:
        os.makedirs(folder, exist_ok=True)

    # Lista cu toate pozele
    all_images = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    # Amestecăm pozele
    random.shuffle(all_images)

    total = len(all_images)
    train_size = int(train_ratio * total)
    validation_size = int(val_ratio * train_size)
    train_actual_size = train_size - validation_size

    # Împărțim pozele
    train_images = all_images[:train_actual_size]
    validation_images = all_images[train_actual_size:train_size]
    test_images = all_images[train_size:]

    # Mutăm fișierele în folderele corespunzătoare
    for img in train_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(train_folder, img))

    for img in validation_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(validation_folder, img))

    for img in test_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(test_folder, img))

    print(f"Total poze: {total}")
    print(f"Train: {len(train_images)}, Validation: {len(validation_images)}, Test: {len(test_images)}")

if __name__ == "__main__":
    source = r"A:\cats_dogs_light\Proiect RN COMARDICI ALEXANDRU\dataset\Sistem inteligent de clasificare a animalelor\data\train"
    output = r"A:\cats_dogs_light\Proiect RN COMARDICI ALEXANDRU\dataset\Sistem inteligent de clasificare a animalelor\data\split_data"
    split_images(source, output)

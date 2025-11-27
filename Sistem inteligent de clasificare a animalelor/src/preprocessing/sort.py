import os

# Setează calea către folderul în care ai pozele
folder_path = r"A:\cats_dogs_light\Proiect RN COMARDICI ALEXANDRU\dataset\train\cat"

# Extensii acceptate
extensii = [".jpg", ".jpeg", ".png"]

# Obține lista de fișiere filtrată doar pe poze
poze = [f for f in os.listdir(folder_path) 
        if os.path.splitext(f)[1].lower() in extensii]

# Sortează lista pentru a avea o ordine constantă
poze.sort()

# Parcurge și redenumește
for index, filename in enumerate(poze, start=1):
    extensie = os.path.splitext(filename)[1]
    new_name = f"cat{index}{extensie}"
    
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    print(f"{filename} -> {new_name}")

print("Redenumirea s-a terminat!")

import os
import pandas as pd
import re

folder_path = r"A:\cats_dogs_light\Proiect RN COMARDICI ALEXANDRU\dataset\train"
output_csv = os.path.join(folder_path, "annotations.csv")

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}

def extract_number(path):
    fname = os.path.basename(path)
    m = re.search(r'(\d+)', fname)
    return int(m.group(1)) if m else float("inf")

def make_relative_path(root_folder, full_path):
    rel = os.path.relpath(full_path, root_folder)
    return rel.replace(os.sep, "/")

def gather_images(folder):
    rows = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for fname in filenames:
            ext = os.path.splitext(fname)[1].lower()
            if ext in IMAGE_EXTS:
                full = os.path.join(dirpath, fname)
                rel = make_relative_path(folder, full)
                species = os.path.basename(os.path.dirname(full))
                rows.append((rel, species))

    # SORTARE: întâi după species, apoi numeric
    def sort_key(row):
        filename, species = row
        species_order = {"cat": 0, "dog": 1}
        sp_key = species_order.get(species.lower(), 2)
        num_key = extract_number(filename)
        return (sp_key, num_key)

    rows.sort(key=sort_key)
    return rows

def generate_csv():
    cols = ["filename", "species", "has_owner", "size"]
    img_list = gather_images(folder_path)

    data = []
    for rel_path, species in img_list:
        data.append({
            "filename": rel_path,
            "species": species,
            "has_owner": "",
            "size": ""
        })

    pd.DataFrame(data, columns=cols).to_csv(output_csv, index=False)
    print("CSV generat:", output_csv)

if __name__ == "__main__":
    generate_csv()

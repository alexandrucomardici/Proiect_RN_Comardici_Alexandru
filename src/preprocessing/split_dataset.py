import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(input_dir, output_dirs, test_size=0.15, val_size=0.15):
    classes = os.listdir(input_dir)

    for cls in classes:
        class_path = os.path.join(input_dir, cls)
        files = [f for f in os.listdir(class_path)]
        
        train, temp = train_test_split(files, test_size=(test_size+val_size), random_state=42)
        val, test = train_test_split(temp, test_size=0.5, random_state=42)

        for name, subset in zip(["train", "validation", "test"], [train, val, test]):
            out = os.path.join(output_dirs[name], cls)
            os.makedirs(out, exist_ok=True)
            for file in subset:
                shutil.copy(os.path.join(class_path, file), out)

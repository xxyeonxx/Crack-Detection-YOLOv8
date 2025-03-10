import os
import shutil
from sklearn.model_selection import train_test_split

def prepare_dataset(source_dir, dest_dir, split=0.2):
    cracked_images = os.listdir(os.path.join(source_dir, "CW"))
    uncracked_images = os.listdir(os.path.join(source_dir, "UW"))

    # Split datasets
    train_cracked, val_cracked = train_test_split(cracked_images, test_size=split, random_state=42)
    train_uncracked, val_uncracked = train_test_split(uncracked_images, test_size=split, random_state=42)

    # Move files
    for category, train_files, val_files in [
        ("cracked", train_cracked, val_cracked),
        ("uncracked", train_uncracked, val_uncracked),
    ]:
        os.makedirs(os.path.join(dest_dir, "train", category), exist_ok=True)
        os.makedirs(os.path.join(dest_dir, "val", category), exist_ok=True)

        for file in train_files:
            shutil.copy(os.path.join(source_dir, category[:1] + "W", file), os.path.join(dest_dir, "train", category))
        for file in val_files:
            shutil.copy(os.path.join(source_dir, category[:1] + "W", file), os.path.join(dest_dir, "val", category))

# Paths
source = "/home/nuclear/Downloads/crack_data/DATA_Maguire_20180517_ALL/SDNET2018"
destination = "/home/nuclear/crack_detection/dataset"
prepare_dataset(source, destination)

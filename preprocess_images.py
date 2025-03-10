import cv2
import os

def preprocess_images(directory, target_size=(640, 640)):
    for subdir, _, files in os.walk(directory):
        for file in files:
            img_path = os.path.join(subdir, file)
            img = cv2.imread(img_path)
            if img is not None:
                img_resized = cv2.resize(img, target_size)
                cv2.imwrite(img_path, img_resized)

# Preprocess train and validation datasets
preprocess_images("crack_detection/dataset/train")
preprocess_images("crack_detection/dataset/val")

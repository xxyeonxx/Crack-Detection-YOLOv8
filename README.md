# Crack Detection with YOLOv8
## A project for detecting cracks in concrete structures using YOLOv8, implemented with a RealSense camera on a Jackal robot.

# Introduction
This project focuses on developing a crack detection system for concrete structures, particularly for nuclear power plants where safety is critical. The system utilizes:

YOLOv8 for real-time crack detection.
Jackal UGV with an Intel RealSense Camera for autonomous movement and data collection.
ROS (Robot Operating System) for robot control.
The goal is to improve the safety and efficiency of infrastructure inspection by enabling autonomous crack detection and monitoring.

# Project Structure
📂 Crack-Detection-YOLOv8
│── 📂 dataset/                 # Dataset (images and labels)
│── 📂 models/                  # Trained YOLOv8 models
│── 📂 outputs/                 # Inference results
│── 📂 runs/                     # YOLO training logs
│── 📂 scripts/                  # Supporting scripts
│── data.yaml                    # YOLO dataset configuration
│── jackal_flowchart.py          # Experiment visualization
│── prepare_dataset.py           # Dataset preprocessing
│── preprocess_images.py         # Image preprocessing script
│── yolov8n.pt                    # YOLOv8 pre-trained model
│── README.md                     # Project documentation


# To set up the environment:
git clone https://github.com/xxyeonxx/Crack-Detection-YOLOv8.git
cd Crack-Detection-YOLOv8
pip install -r requirements.txt  # If applicable


# Dataset
The dataset includes 500 images: cracked vs. uncracked concrete surfaces.
Labeled using Roboflow.
Dataset structure follows the YOLO format:

dataset/
├── train/
│   ├── images/
│   ├── labels/
├── val/
│   ├── images/
│   ├── labels/

YAML configuration (data.yaml):
train: dataset/train/images
val: dataset/val/images
nc: 1
names: ["Cracks"]

# Training
To train the YOLOv8 model:

yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=150 imgsz=256
Image size: 256x256
Augmentations: Enabled (flipping, brightness)
Epochs: 150

# Results
First trial: 640x640, no augmentations, 50 epochs → Poor results
Second trial: 256x256, with augmentations, 100 epochs → Improved
Third trial: 256x256, with augmentations, 150 epochs → Best performance

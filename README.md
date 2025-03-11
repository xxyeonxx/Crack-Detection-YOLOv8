# Crack Detection with YOLOv8
## A project for detecting cracks in concrete structures using YOLOv8, implemented with a RealSense camera on a Jackal robot.

## Introduction
This project focuses on developing a crack detection system for concrete structures, particularly for nuclear power plants where safety is critical. 
The goal is to improve the safety and efficiency of infrastructure inspection by enabling autonomous crack detection and monitoring.
The system utilizes:

# YOLOv8 for real-time crack detection.
# Jackal UGV 
with an Intel RealSense Camera for autonomous movement and data collection.
![Jackal](jackal.png)

# ROS (Robot Operating System) for robot control.


## Project Structure
- **Crack-Detection-YOLOv8/**
  - `dataset/` - Contains images and labels
  - `models/` - Trained YOLOv8 models
  - `outputs/` - Inference results
  - `runs/` - YOLO training logs
  - `scripts/` - Supporting scripts
  - `data.yaml` - YOLO dataset configuration
  - `jackal_flowchart.py` - Experiment visualization
  - `prepare_dataset.py` - Dataset preprocessing
  - `preprocess_images.py` - Image preprocessing script
  - `yolov8n.pt` - YOLOv8 pre-trained model
  - `README.md` - Project documentation



## To set up the environment:
# Clone the repository:
```git clone https://github.com/xxyeonxx/Crack-Detection-YOLOv8.git```
# Install dependencies:
```pip install -r requirements.txt  # If applicable```


## Dataset
The dataset consists of 500 images, including cracked and uncracked surfaces. Images were labeled using Roboflow.

- **Dataset Structure** (YOLO format):
```
dataset/
├── train/
│   ├── images/
│   └── labels/
└── val/
    ├── images/
    └── labels/
``` 

- **Labels**: YOLO format (`data.yaml`):
```yaml
train: dataset/train/images
val: dataset/val/images
nc: 1
names: ["Cracks"]
```
## Annotations
Manual annotation with Roboflow, labeling cracks with bounding boxes.
(Class : Crack)
![Annotaions](labeling_roboflow.png)

## Training
# To train the YOLOv8 model, run:
```yolo train data=data.yaml model=yolov8n.pt epochs=150 imgsz=256```


## Results
- **First trial**: `640x640`, `50 epochs` → Poor results
- **Second trial**: `256x256`, `100 epochs` → Improved
- **Third trial**: `256x256`, `150 epochs` → Best performance

## Experiments
1. Run the Jackal Robot
   - You need to launch the Jackal's ROS environment and pair the joystick to control it.
     ```
     roslaunch jackal_control teleop.launch
     ```
2. Run the Crack Detection Model
3. 

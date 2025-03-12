## Crack Detection with YOLOv8
- A project for **detecting cracks in concrete structures** using YOLOv8, implemented with a RealSense camera on a Jackal robot.

## Introduction
- Ensuring the structural health of concrete infrastructures is crucial, especially in **nuclear power plants**, where cracks can lead to catastrophic failures. Traditionally, human inspectors conduct periodic visual assessments, which are time-consuming and risky.
- This project focuses on automating crack detection using an autonomous robotic system, leveraging state-of-the-art deep learning models.
- By integrating **YOLOv8 for real-time crack detection** with the **Jackal and Intel RealSense Camera**, we enable remote, efficient, and continuous monitoring of infrastructure. The **Robot Operating System (ROS)** facilitates robot control and real-time data collection, allowing seamless deployment in hazardous environments.
- The goal is to **improve the safety and efficiency of infrastructure inspection** by enabling autonomous crack detection and monitoring.


- The system utilizes:
  - **YOLOv8** for real-time crack detection.
  - **Jackal UGV** 
    with an Intel RealSense Camera for autonomous movement and data collection.
    ![Jackal](jackal.png)
  - **ROS (Robot Operating System)** for robot control.

## Benefits
- This project also explores **Human-Robot Interaction (HRI)** by examining how robotic-assisted inspections can complement and **improve human's safety.**
- The key benefits include:

  🔍 Enhanced Inspection Capabilities:
    The robot autonomously navigates through structures and detects cracks in real-time, providing live feedback to human operators.

  🛠 Operator-Assisted Control:
    Instead of fully replacing human inspectors, the robot serves as an intelligent assistant, helping experts focus on analyzing critical defects rather than performing repetitive manual     inspections.

  🚧 Increased Safety & Reduced Exposure:
    In high-risk environments, such as nuclear power plants, oil refineries, or bridges, sending a robot for preliminary inspections minimizes human exposure to radioactive or structurally compromised areas.

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
- Clone the repository:
  ```
  git clone https://github.com/xxyeonxx/Crack-Detection-YOLOv8.git
  cd Crack-Detection-YOLOv8
  ```
- Install dependencies:
  ```
  pip install -r requirements.txt  # If applicable
  ```


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

| Trial  | Image Size | Epochs | Precision | Recall | mAP@50 | mAP@50-95 |
|--------|-----------|--------|-----------|--------|--------|-----------|
| First  | 640x640   |  50    |  0.65     |  0.52  |  0.55  |  0.30     |
| Second | 256x256   | 100    |  0.71     |  0.58  |  0.68  |  0.48     |
| Third  | 256x256   | 150    |  0.81     |  0.65  |  0.73  |  0.52     |

- **Precision**: Measures how many of the detected cracks are actually cracks.
- **Recall**: Measures how many actual cracks were detected.
- **mAP@50**: Mean Average Precision at IoU 0.5 (general accuracy).
- **mAP@50-95**: Mean Average Precision across different IoU thresholds (stricter accuracy).

📌 *The third trial performed the best with higher precision and recall!* 🚀

## Experiments
1. Run the Jackal Robot
  - To operate Jackal and manually control it via a joystick:
     ```
     roslaunch jackal_control teleop.launch
     ```
2. Run the Crack Detection Model
  - To start real-time crack detection on Jackal, run:
   
     ```
     python3 crack_detection.py
     ```
  - This script:
      - Captures real-time video from the Intel RealSense Camera.
      - Runs YOLOv8 inference on each frame.
      - Displays detected cracks with bounding boxes.


3. Monitor your model's performance
  - Example of crack detection output:
    ![Monitor](crack_detection_screenshot.png)


5. Refine your results


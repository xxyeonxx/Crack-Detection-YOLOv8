#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
import pyrealsense2 as rs
from ultralytics import YOLO
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class CrackDetectionNode:
    def __init__(self):
        rospy.init_node("crack_detection_node", anonymous=True)

        # ROS subscribers and publishers
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.image_callback)
        self.image_pub = rospy.Publisher("/crack_detection/output", Image, queue_size=1)

        # Load YOLO Model
        model_path = "/home/nuclear/catkin_ws/src/crack_detection_ros/model/best.pt"  # Adjust path
        self.model = YOLO(model_path)

    def image_callback(self, msg):
        try:
            # Convert ROS Image to OpenCV format
            frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")

            # Convert to grayscale and resize
            grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resized_frame = cv2.resize(grayscale_frame, (256, 256))
            resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_GRAY2BGR)

            # Run YOLO inference
            results = self.model(resized_frame, conf=0.55)

            # Draw bounding boxes
            for result in results[0].boxes:
                box = result.xyxy[0].cpu().numpy().astype(int)
                conf = result.conf[0]
                label = f"Crack {conf:.2f}"

                x1, y1, x2, y2 = box
                cv2.rectangle(resized_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(resized_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Publish the processed image
            output_msg = self.bridge.cv2_to_imgmsg(resized_frame, "bgr8")
            self.image_pub.publish(output_msg)

            # Display (optional)
            cv2.imshow("Crack Detection Output", resized_frame)
            cv2.waitKey(1)

        except Exception as e:
            rospy.logerr(f"Error processing image: {e}")

if __name__ == "__main__":
    try:
        CrackDetectionNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        cv2.destroyAllWindows()


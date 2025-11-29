# 🚗 Vehicle Counting using YOLO and Object Tracking

This project implements a **vehicle counting system** using a YOLO-based object detection model combined with object tracking.
The system counts vehicles (cars, buses, trucks) in a video by detecting them and tracking their movement across a predefined counting line.

## 🎯 Objective

To understand and implement:

* Object detection using **YOLO**
* Object tracking for maintaining object identities
* Motion-based counting using line-crossing logic
* Video processing using OpenCV

## ⚙️ How it works

1. A traffic video is taken as input.
2. YOLO detects vehicles in each frame.
3. A tracker assigns **unique IDs** to detected vehicles.
4. Each vehicle’s center is tracked across frames.
5. A count is incremented when a vehicle crosses a predefined line.
6. The output video is saved with bounding boxes, IDs, and vehicle count shown.
 
## 🧠 Key Concepts Used

* YOLO object detection
* Tracking-by-detection
* Line-crossing logic for counting
* Frame-wise video processing with OpenCV

## 🛠️ Tech Stack

* Python
* OpenCV
* Ultralytics YOLO (YOLOv8)
* NumPy

## ▶️ How to Run

1. Place the input video in the project directory.
2. Install dependencies:

   ```bash
   pip install ultralytics opencv-python
   ```
3. Run the script:

   ```bash
   python car_counting.py
   ```
4. The processed output video will be saved locally.

## 📌 Notes

* This project is intended for **learning and experimentation**.
* Performance depends on system capability and video resolution.
* For edge deployment (e.g., Raspberry Pi), further optimization is required.

## 📄 License

This project is for educational purposes.

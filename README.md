# ARC Computer Vision Workshop

Welcome to the ARC Computer Vision Workshop! This repository contains example scripts and materials to introduce fundamental computer vision concepts with the help of [OpenCV](https://opencv.org/). The workshop is designed to be around two hours in length, including presentations and hands-on coding exercises.

## Overview

1. **Installation**  
   - Clone this repository  
   - 
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   
2. **Basic Concepts**  
   - **Image representation**: Images can be thought of as multi-dimensional arrays (e.g., height × width × channels).
   - **Color spaces**: RGB (Red, Green, Blue), Grayscale, HSV, etc.
   - **Transformations**: Scaling, translation, rotation.
   - **Filtering**: Gaussian blur, median blur, etc.
   - **Edge Detection**: Identifying boundaries in images (Canny, Sobel, etc.).

3. **Scripts**  
   - `scripts/basic_opencv.py`: Simple demonstration of how to load, display, and save images using OpenCV.  
   - `scripts/edge_detection.py`: Example of edge detection using Canny.

4. **Project**  
   - At the end of this workshop, participants will create a mini-project applying these techniques to a real-world or fun dataset. More details will be provided in the workshop slides.

## Further Reading

- **OpenCV Documentation**: [docs.opencv.org](https://docs.opencv.org/)  
- **Image Processing and Computer Vision Basics**:  
  - [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)

## Getting Started

1. Make sure you have Python 3.8+ installed.  
2. Clone this repo and install the dependencies:
   ```bash
   git clone https://github.com/purdue-arc/cv_workshop.git
   cd cv_workshop
   pip install -r requirements.txt
3. Run any of the scripts in the `scripts/` folder:
   This script shows a live grayscale version of your video stream.
   ```bash
   python scripts/basic_opencv.py
   ```

   This script shows a screen containing edge detections from your live video stream.
   ```bash
   python scripts/edge_detection.py
   ```

   This script shows a simple YOLOv8 Detection running through the ultralytics package. One could also run a more general, pre-trained YOLOv8 with the `inference` package: [YOLOv8 Website instructions](https://yolov8.com/)
   ```bash
   python scripts/yolov8_detection.py
   ```

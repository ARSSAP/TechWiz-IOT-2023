
## Features: 
* Obstacle Detection, Classification and Localization.
* Voice Feedback through Earphones regarding the detected Obstacles.
* Distance Measuring using Ultrasonic Sensor.
* Live Video as well as Still Image capture using Pi Camera for processing.
* Push Buttons to choose specific mode while navigation.

**Detailed Thesis and working has been provided in the thesis report in the Repository.**
## Technology Stack
* Python+Flask Server for API requests
* OpenCV for Image Recognition
* YOLO for Realtime Object Recognition

## Hardware Components
* Rasperry Pi 4 Model B
* water Level Sensor
* PIR sensor 
* Audio Sensor
* Raspberry Pi Camera V2
* Connecting Wires
* Battery Backup


## Working
In this project we will be processing images taken through Pi Camera mounted on our
smart Blind Stick. In the Object Detection Mode the Obstacles in front of the
blind person will be captured, the results of image processing will consist of Detected
Objects along with their spatial location. We will be processing still images using our
self developed API hosted on Heroku, the results will then be converted to an
audio feedback using python ESpeak module and will be fed into the earphones of the
user. The live video will be processed using OpenCV libraries and SSD MobileNet
Lite algorithm on real time frames to produce detections.This mode is active when we
press the Navigation button on the stick.


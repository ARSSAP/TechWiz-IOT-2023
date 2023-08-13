import time
import picamera

# Create a camera object
camera_sensor = picamera.PiCamera()

try:
    print("Recording video...")
    
    # Start recording a video and save it to the specified file
    camera_sensor.start_recording('video.h264')
    
    # Record for 10 seconds (adjust as needed)
    camera_sensor.wait_recording(10)
    
    # Stop recording
    camera_sensor.stop_recording()
    
    print("Video recorded: video.h264")

finally:
    # Clean up and release camera resources
    camera_sensor.close()

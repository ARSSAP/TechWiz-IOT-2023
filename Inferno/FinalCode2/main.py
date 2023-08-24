import cv2
import imutils
import numpy as np

# Load YOLOv3 model and coco.names labels
net = cv2.dnn.readNet("model2-files/yolov3.weights", "model1-files/yolov3.cfg")
labels = open("model2-files/coco.names").read().strip().split("\n")
layer_names = net.getUnconnectedOutLayersNames()

# Initialize Pi Camera
camera = cv2.VideoCapture(0)  # Use 0 for the first camera

while True:
    ret, frame = camera.read()
    if not ret:
        break
    
    # Resize frame for faster processing
    frame = imutils.resize(frame, width=800)
    
    # Perform object detection
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(layer_names)
    
    # Process detection results
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > 0.5:  # Set a confidence threshold
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])
                
                x = int(center_x - width / 2)
                y = int(center_y - height / 2)
                
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
                cv2.putText(frame, labels[class_id], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Object Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

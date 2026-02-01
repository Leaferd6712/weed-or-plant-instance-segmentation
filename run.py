from ultralytics import YOLO

# Load pretrained YOLOv8s-seg pothole model
model = YOLO("best.pt")

# Run webcam instance segmentation
model.predict(source=0, show=True)

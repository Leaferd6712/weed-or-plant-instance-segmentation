from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(
    source="0",  # or full path if you prefer
    show=True,
    save=True            # <— this makes YOLO save the processed video

)



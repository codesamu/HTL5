from ultralytics import YOLO
import torch

# Select training device
if torch.backends.mps.is_available():
    device = "mps"
    print("Using Apple GPU (MPS)")
else:
    device = "cpu"
    print("Using CPU")

# Load pretrained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Start training
results = model.train(
    data="school_objects/dataset.yaml",
    epochs=15,
    imgsz=640,
    batch=8,
    device=device,
    workers=2,
    project="runs/detect",
    name="school_objects",
    plots=True
)

print("Training finished!")
print("Best model saved in:")
print("runs/detect/school_objects/weights/best.pt")

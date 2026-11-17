import cv2
from ultralytics import YOLO
from pathlib import Path

# --------------------------------------------------
# 1. Find the trained model automatically
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

possible_paths = [
    BASE_DIR / "runs/detect/school_objects/weights/best.pt",
    BASE_DIR.parent / "runs/detect/runs/detect/school_objects-3/weights/best.pt",
    Path.home() / "HTL5/runs/detect/runs/detect/school_objects-3/weights/best.pt",
]

MODEL_PATH = next(
    (path for path in possible_paths if path.exists()),
    None
)

if MODEL_PATH is None:
    raise FileNotFoundError(
        "Could not find best.pt. Check your training output folder."
    )

print(f"Loading model: {MODEL_PATH}")

# --------------------------------------------------
# 2. Load custom YOLO model
# --------------------------------------------------

model = YOLO(str(MODEL_PATH))

print("Model loaded successfully!")
print("Classes:", model.names)

# --------------------------------------------------
# 3. Open Mac webcam
# --------------------------------------------------

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("ERROR: Cannot open webcam.")
    print("Try changing camera index from 0 to 1.")
    exit()

print("Webcam started!")
print("Press Q to quit.")

# --------------------------------------------------
# 4. Real-time object detection
# --------------------------------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        print("ERROR: Cannot read webcam frame.")
        break

    results = model.predict(
        source=frame,
        conf=0.25,
        imgsz=640,
        verbose=False
    )

    # Draw bounding boxes and labels
    annotated_frame = results[0].plot()

    cv2.imshow(
        "Custom YOLO - School Object Detection",
        annotated_frame
    )

    # Quit with Q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# --------------------------------------------------
# 5. Clean up
# --------------------------------------------------

cap.release()
cv2.destroyAllWindows()

print("Webcam closed.")


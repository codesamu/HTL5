import cv2
from ultralytics import YOLO

# Load pretrained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Open Mac webcam using native macOS camera interface
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# Check if camera opened
if not cap.isOpened():
    print("ERROR: Cannot open webcam.")
    print("Try changing camera index from 0 to 1.")
    exit()

print("Webcam started! Press Q to quit.")

while True:
    # Read webcam frame
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Cannot read webcam frame.")
        break

    # Detect persons (COCO class 0)
    results = model.predict(
        source=frame,
        classes=[0],
        conf=0.5,
        verbose=False
    )

    # Draw bounding boxes and labels
    annotated_frame = results[0].plot()

    # Display webcam
    cv2.imshow("YOLOv8 - Person Detection", annotated_frame)

    # Quit when Q is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Webcam closed.")


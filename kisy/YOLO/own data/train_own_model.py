#!/usr/bin/env python3
"""Step 3 - train YOLOv8n on the own-objects dataset (bottle + pen).

Run from the yolo/ folder:  venv/bin/python "own data/train_own_model.py"
Results -> own data/runs/train/  (weights: weights/best.pt)
"""
from pathlib import Path
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent
model = YOLO(str(ROOT.parent / "yolov8n.pt"))
model.train(
    data=str(ROOT / "dataset" / "data.yaml"),
    epochs=20, imgsz=640, batch=16, device="mps",
    project=str(ROOT / "runs"), name="train", exist_ok=True, seed=0,
)

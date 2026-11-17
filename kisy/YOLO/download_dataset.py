import fiftyone.zoo as foz
import fiftyone as fo

# Classes we want to detect
classes = [
    "bottle",
    "cell phone",
    "cup",
    "book",
    "laptop",
    "scissors"
]

# Download training and validation datasets
for split in ["train", "validation"]:

    print(f"\nDownloading {split} dataset...")

    ds = foz.load_zoo_dataset(
        "coco-2017",
        split=split,
        label_types=["detections"],
        classes=classes,
        max_samples=1500
    )

    # Export dataset in YOLO format
    ds.export(
        export_dir="school_objects",
        dataset_type=fo.types.YOLOv5Dataset,
        label_field="ground_truth",
        classes=classes,
        split="val" if split == "validation" else "train"
    )

    print(f"{split} dataset exported successfully!")

print("\nDataset download and export complete!")

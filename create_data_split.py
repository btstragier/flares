import random
import shutil
from pathlib import Path

SOURCE_DIR = Path("frames")      # your current directory
OUTPUT_DIR = Path("flares_yolo")      # new YOLO dataset root
TRAIN_RATIO = 0.8
SEED = 42

def main():
    random.seed(SEED)

    images = sorted(SOURCE_DIR.glob("*.jpg"))

    # Only keep images that have matching label files
    pairs = []
    for img in images:
        label = img.with_suffix(".txt")
        if label.exists():
            pairs.append((img, label))

    if not pairs:
        raise RuntimeError("No image/label pairs found")

    random.shuffle(pairs)

    split_idx = int(len(pairs) * TRAIN_RATIO)
    train_pairs = pairs[:split_idx]
    val_pairs = pairs[split_idx:]

    for split_name, split_pairs in [("train", train_pairs), ("val", val_pairs)]:
        img_out = OUTPUT_DIR / "images" / split_name
        lbl_out = OUTPUT_DIR / "labels" / split_name
        img_out.mkdir(parents=True, exist_ok=True)
        lbl_out.mkdir(parents=True, exist_ok=True)

        for img, lbl in split_pairs:
            shutil.copy2(img, img_out / img.name)
            shutil.copy2(lbl, lbl_out / lbl.name)

    print(f"Total pairs: {len(pairs)}")
    print(f"Train: {len(train_pairs)}")
    print(f"Val: {len(val_pairs)}")
    print("Done.")

if __name__ == "__main__":
    main()

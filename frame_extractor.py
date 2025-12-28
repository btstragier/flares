import cv2
import os

video_path = "train_video.mp4"
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_idx = 0
save_every = 10
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_idx % save_every == 0:
        count += 1
        cv2.imwrite(
            os.path.join(output_dir, f"frame_{frame_idx:06d}.jpg"),
            frame
        )

    frame_idx += 1
print(f'Total number of frames: {count}')
cap.release()

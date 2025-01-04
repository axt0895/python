from ultralytics import YOLO

model = YOLO('yolov10l')

results = model.predict('input_videos/premier_league_30.mp4', save = True)

for boxes in results[0]:
    print(boxes)
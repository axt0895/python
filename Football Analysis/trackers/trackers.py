from ultralytics import YOLO
import supervision as sv
import pickle
import os


class Tracker:
    
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()
    
    def detect_frames(self, frames):
        batch_size = 32
        detections = []
        
        for i in range(0, len(frames), batch_size):
            detection_batch = self.model.predict(frames[i:i+batch_size], conf = 0.2)
            detections += detection_batch
        return detections

    def get_object_track(self, frames, read_from_stub=False, stub_path = None):
        
        if read_from_stub and stub_path is not None and os.path.exists(stub_path):
            with open(stub_path, 'rb') as file:
                tracks = pickle.load(file)
            return tracks
            
        detections = self.detect_frames(frames)
        tracks = {
            "Football": [],
            "Player": [],
            "refere":[]
        }
        
        for frame_num, detection in enumerate(detections):
            class_names = detection[0].names
            class_names_inv = {v:k for k, v in class_names.items()}
            
            #  Convert to supervision detection format
            detection_supervision = sv.Detections.from_ultralytics(detection)
            
            # Track Objects
            detection_with_tracks = self.tracker.update_with_detections(detection_supervision)
            
            tracks["Football"].append({})
            tracks["Player"].append({})
            tracks["refere"].append({})
            
            for frame_detection in detection_with_tracks:
                bbox = frame_detection[0].tolist()
                class_id = frame_detection[3]
                tracker_id = frame_detection[4]
                
                if class_id == class_names_inv['Player']:
                    tracks['Player'][frame_num][tracker_id] = {'bbox': bbox}
                if class_id == class_names_inv['refere']:
                    tracks['refere'][frame_num][tracker_id] = {'bbox': bbox}
            
            for frame_detection in detection_supervision:
                bbox = frame_detection[0].tolist()
                class_id = frame_detection[3]
                if class_id == class_names_inv['Football']:
                    tracks['Football'][frame_num][1] = {'bbox': bbox}
        if stub_path is not None:
            with open(stub_path, 'wb') as file:
                pickle.dump(tracks, file)
        return tracks
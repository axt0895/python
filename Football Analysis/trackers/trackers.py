from ultralytics import YOLO
import supervision as sv



class Tracker:
    
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()
    
    def detect_frames(self, frames):
        batch_size = 20
        detections = []
        
        for i in range(0, len(frames), batch_size):
            detection_batch = self.model.predict(frames[i:i+batch_size], conf = 0.2)
            detections += detection_batch
        return detections
        
    def get_object_tracker(self, frames):
        detections = self.detect_frames(frames)
        
        for frame_num, detection in enumerate(detections):
            
            # Access class names from the model
            class_names = self.model.names
            class_name_inv = {v:k for k, v in class_names.items()}
            
            # Convert YOLO detection to supervision format
            detection_supervision = sv.Detections.from_ultralytics(detection)
            
            # Track objects using ByteTrack
            tracked_objects = self.tracker.update_with_detections(detection_supervision)
            
        
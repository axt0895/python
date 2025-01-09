from ultralytics import YOLO
import supervision as sv
import pickle
import cv2
import os
import sys

sys.path.append('../')
from utils import get_center_bbox, get_bbox_width


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
    
    def draw_ellipse(self, frame, bbox, color, track_id):
        y2 = int(bbox[3])
        x_center, _ = get_center_bbox(bbox)
        width = get_bbox_width(bbox)
        cv2.ellipse(
            frame, 
            center= (x_center, y2),
            axes=(int(width), int(0.35 * width)),
            angle=0.0,
            startAngle=-45,
            endAngle=235,
            color=color,
            thickness=2
        )
        
        return frame
        
        
    
    def draw_annotation(self, video_frames, tracks):
        output_video_frames = []
        
        for frame_num, frame in enumerate(video_frames):
            frame = frame.copy()
            
            player_dict = tracks['Player'][frame_num]
            football_dict = tracks['Football'][frame_num]
            refere_dict = tracks['refere'][frame_num]
            
            # Draw players
            for track_id, player in player_dict.items():
                frame = self.draw_ellipse(frame, player['bbox'], (0, 0, 255), track_id)
            output_video_frames.append(frame)
        return output_video_frames
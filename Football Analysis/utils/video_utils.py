import cv2
'''
- This method reads a given video and writes each frame to a list and returns it
'''
def read_video(video_file_path):
    frames = []
    capture = cv2.VideoCapture(video_file_path)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        frames.append(frame)
    return frames

'''
- This method takes a list of frames and output a video
'''

import cv2

def save_video(output_video_frames, output_video_path):
    if not output_video_frames:
        return
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    height, width = output_video_frames[0].shape[:2]
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))
    
    for frame in output_video_frames:
        out.write(frame)
    
    out.release()

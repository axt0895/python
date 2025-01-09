from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read video
    video_frames = read_video('/Users/anilthapa/python/Football Analysis/input_videos/premier_league_30.mp4')
    
    # Initialize the Tracker
    tracker = Tracker('/Users/anilthapa/Downloads/best.pt')
    
    tracks = tracker.get_object_track(video_frames, read_from_stub = True, stub_path = '/Users/anilthapa/python/Football Analysis/stubs/track_stubs.pkl')
    
    # Save video
    save_video(video_frames, '/Users/anilthapa/python/Football Analysis/output_videos/detect.avi')


if __name__ == '__main__':
    main()
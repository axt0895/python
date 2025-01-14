from utils import read_video, save_video
from trackers import Tracker

def main():
    # Read video
    premier_league = '/Users/anilthapa/python/Football Analysis/input_videos/premier_league_30.mp4'
    world_cup = '/Users/anilthapa/world_cup.mp4'
    video_frames = read_video('/Users/anilthapa/world_cup_10_second.mp4')
    
    # Initialize the Tracker
    tracker = Tracker('/Users/anilthapa/Downloads/last.pt')
    
    tracks = tracker.get_object_track(video_frames, read_from_stub = True, stub_path = '/Users/anilthapa/python/Football Analysis/stubs/track_stubs.pkl')
    
    # Draw object track
    output_video_frames = tracker.draw_annotation(video_frames, tracks)
    
    # Save video
    save_video(output_video_frames, '/Users/anilthapa/python/Football Analysis/output_videos/detect.avi')


if __name__ == '__main__':
    main()
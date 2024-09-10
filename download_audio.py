from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable

import sys

OUTPUT_PATH = './Downloaded audios'

def start_download(video: YouTube):
    print(f'Title: {video.title}')

    try:
        audio = video.streams.get_audio_only()

    except Exception as e:
        return e
    
    else:
        print("Starting download...")
        audio.download(OUTPUT_PATH, mp3=True)
        print("Audio download complete.")

def download_audio(url: str):
    try:
        video = YouTube(url)
    
    except VideoUnavailable:
        print("Unable to fetch video...")
        sys.exit(1)

    else:
        start_download(video)


def main():
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_audio(video_url)
        
    else:
        print("Please provide a video URL.")

if __name__ == '__main__':
    main()
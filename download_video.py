from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable

import sys

OUTPUT_PATH = './Downloaded videos'
VIDEO_RES = '360p'

def start_download(video: YouTube):
    print(f'Title: {video.title}')

    try:
        vid = video.streams.filter(res=VIDEO_RES, progressive=True).first()

    except Exception as e:
        return e
    
    else:
        print("Starting download...")
        vid.download(OUTPUT_PATH)
        print("Video download complete.")

def download_video(url: str):
    try:
        video = YouTube(url)
    
    except VideoUnavailable:
        print("Unable to download video...")
        sys.exit(1)

    else:
        start_download(video)


def main():
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_video(video_url)
        
    else:
        print("Please provide a video URL.")

if __name__ == '__main__':
    main()
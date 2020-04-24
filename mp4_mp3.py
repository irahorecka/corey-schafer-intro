"""Convert mp4 files to mp3 -- change directories as
you like"""
import os
from moviepy.editor import *
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # directory with scraped playlist videos
CLIPPED_DIR = f"{BASE_DIR}/clipped_audio"


def mp4_mp3(FILE_DIR):
    """Convert mp4 files from clipped_audio/mp4
    to mp3 in clipped_audio/mp3 directory"""
    MP4_DIR = f"{FILE_DIR}/mp4"
    try:
        MP3_DIR = f"{FILE_DIR}/mp3"
        os.mkdir(MP3_DIR)
    except FileExistsError:
        pass
    
    os.chdir(MP4_DIR)
    for file in os.listdir():
        if file[-4:] == '.mp4':
            video = AudioFileClip(file)
            video.write_audiofile(f"{MP3_DIR}/{file[:-4]}.mp3")


if __name__ == "__main__":
    mp4_mp3(CLIPPED_DIR)

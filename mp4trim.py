"""Trim mp4 files to given start and stop seconds.
Store trimmed mp4 files to directory clipped_audio."""
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # i.e. directory with source mp4 files


def clip_mp4(start_time, end_time):
    """Extract fixed segments of mp4 files
    from current directory and move segments
    to "clipped_audio" folder"""
    CLIPPED_DIR = f"{BASE_DIR}/clipped_audio"
    try:
        os.mkdir(CLIPPED_DIR)
        CLIPPED_DIR_MP4 = f"{CLIPPED_DIR}/mp4"
        os.mkdir(CLIPPED_DIR_MP4)
    except FileExistsError:
        pass

    # opening file and extracting segment - place in clipped_audio directory
    for file in os.listdir(BASE_DIR):
        if file[-4:] == '.mp4':
            ffmpeg_extract_subclip(file, start_time, end_time, targetname=f"{CLIPPED_DIR_MP4}/clipped_{file[:-4]}.mp4")


if __name__ == "__main__":
    # start_time, end_time are in seconds
    clip_mp4(start_time=0, end_time=3)

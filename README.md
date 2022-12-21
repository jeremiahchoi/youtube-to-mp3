# youtube-to-mp3
This repository contains a python script to convert video to mp3. We plan to extend it further so that we can download the appropriate video from the church website and convert it to mp3.

# Prerequisites
- Python 3
- ffmpeg

# (Optional) Using python script to download videos
1. To install Pytube using pip, you will need to open your command prompt CLI as an administrator and enter the following command:
```
pip install pytube
```
2. Use this download.py script
```
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
```
3. To run, type the following:
```
python3 download.py
```

# Instructions
1. Download video in same directory as youtube-to-mp3 python script (Video is downloaded as a .mp4 file).
1. On Line 5, replace title with actual name of the video file (include spaces).
2. On Line 5, replace time stamps for portion of video you want audio for.
3. To run, type the following:
```
python3 main.py
```
4. Delete .mp4 video file from directory so that you can download the next video.

# Sample

    vids = dict({"My Video": ("00:01:00","00:02:00")

- "My Video" is the name of the video file.
- The first time stamp "00:01:00" indicates that the audio will start at the 1 minute mark of the video. 
- The second time stamp "00:02:00" indicates that the audio will end at the 2 minute mark of the video.

# From ChatGPT

This script uses the ffmpeg command line tool to convert videos to the MP3 audio format. It has a dictionary called vids that maps the names of the videos to tuples containing start and end times for trimming the audio.

The convert_vid function iterates over the dictionary, using the key as the name of the input video file (vid_name) and the value as the start and end times for trimming (val). It then calls ffmpeg to convert the input video file to an MP3 file with the same name (out_name). It then calls ffmpeg again to trim the audio file between the start and end times specified in the val tuple and save the trimmed audio file with the name out_trimmed_name.

The script also has an if block at the bottom that calls the convert_vid function when the script is run.

Note: This script assumes that the ffmpeg tool is installed on the machine running the script and is available in the system's PATH. It also assumes that the input video files and the script are in the same directory.

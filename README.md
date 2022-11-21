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
4. Delete .mp4 video file.

# Sample

    vids = dict({"My Video": ("00:01:00","00:02:00")

- "My Video" is the name of the video file.
- The first time stamp "00:01:00" indicates that the audio will start at the 1 minute mark of the video. 
- The second time stamp "00:02:00" indicates that the audio will end at the 2 minute mark of the video.

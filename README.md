# youtube-to-mp3
This repository contains a python script to convert video to mp3. We plan to extend it further so that we can download the appropriate video from the church website and convert it to mp3.

# Prerequisites
- Python 3
- ffmpeg

# Instructions
1. Download video in same directory as youtube-to-mp3 python script.
1. On Line 5, replace title with actual name of the video file (include spaces).
2. On Line 5, replace time stamps for portion of video you want audio for.
3. To run, type the following:
```
python3 main.py
```

# Sample

    vids = dict({"My Video": ("00:01:00","00:02:00")

- "My Video" is the name of the video file.
- The first time stamp "00:01:00" indicates that the audio will start at the 1 minute mark of the video. 
- The second time stamp "00:02:00" indicates that the audio will end at the 2 minute mark of the video.

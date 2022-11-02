import os
import subprocess
def convert_vid():
    print("video conversion")
    vids = dict({"Follow Jesus in His Suffering": ("00:01:00","00:02:00"),
                 })
    for key in vids:
        vid_name = key+".mp4"
        out_name = key+".mp3"
        out_trimmed_name = key+"_trimmed.mp3"
        val = vids[key]
        subprocess.call(['ffmpeg','-i',vid_name,out_name])
        subprocess.call(['ffmpeg', '-i', out_name, '-ss', val[0], '-to', val[1], '-acodec', 'copy', out_trimmed_name])

if __name__ == '__main__':
    convert_vid()

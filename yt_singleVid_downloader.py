#YouTube Single Video Downloader

from pytube import YouTube
import os
import re

def sanitize_filename(filename):
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized

##Replicate and Insert your desired YouTube Video URL
video_url = ""

#Replicate and Insert your desired Location to save the Video
output_directory = r""  

try:
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    title = sanitize_filename(yt.title)
    output_filename = f"{title}.mp4"
    video_path = os.path.join(output_directory, output_filename)
    stream.download(output_path=output_directory, filename=output_filename)
    print(f"Downloaded {yt.title}.")
except Exception as e:
    print(f"Error Downloading {video_url}: {e}")
    import traceback
    traceback.print_exc()

print("Video Downloaded Successfully")
# Youtube Playlist Downloader

from pytube import YouTube, Playlist
import os
import re

def sanitize_filename(filename):
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized

#Replicate and Insert your desired YouTube Playlist URL
playlist_url = ""

playlist = Playlist(playlist_url)
video_urls = playlist.video_urls

#Replicate and Insert your desired Location to save Playlist Videos
output_directory = r""

for index, video_url in enumerate(video_urls, start=1):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        title = sanitize_filename(yt.title)
        output_filename = f"{index}){title}.mp4"
        video_path = os.path.join(output_directory, output_filename)
        stream.download(output_path=output_directory, filename=output_filename)
        print(f"Downloaded {index}){yt.title}.")
    except Exception as e:
        print(f"Error Downloading {index}){video_url}: {e}")
        import traceback
        traceback.print_exc()

print("All Videos Downloaded Successfully")
import os
import yt_dlp
from PIL import Image
import tkinter as tk
from tkinter import Entry, Button, Label
import subprocess

def download(playlist_url):
    # Specify the output directory
    output_directory = 'downloads'
    os.makedirs(output_directory, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'EmbedThumbnail',
            },
            {
                'key': 'FFmpegMetadata',
            },
        ],
        'outtmpl': os.path.join(output_directory, '%(title)s.%(ext)s'),
        'writethumbnail': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
        print("hello")

def on_download_click():
    playlist_url = url_entry.get()
    download(playlist_url)
    status_label.config(text="Download complete!")

# Create the main application window
app = tk.Tk()
app.title("YouTube Playlist Downloader")

# Create and place widgets in the window
url_label = Label(app, text="Enter Playlist URL:")
url_label.pack(pady=10)

url_entry = Entry(app, width=40)
url_entry.pack(pady=10)

download_button = Button(app, text="Download", command=on_download_click)
download_button.pack(pady=20)

status_label = Label(app, text="")
status_label.pack()

# Start the Tkinter event loop
app.mainloop()


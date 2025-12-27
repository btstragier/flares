from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=VIDEO_ID"

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

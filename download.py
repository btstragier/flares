from yt_dlp import YoutubeDL

url = "https://www.youtube.com/watch?v=bGO8aH4-k0o&t=26s"

ydl_opts = {
    "format": "bestvideo[ext=mp4]/best[ext=mp4]",
    "outtmpl": "%(title)s.mp4",
    "merge_output_format": "mp4",
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
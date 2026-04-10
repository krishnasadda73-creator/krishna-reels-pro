import requests
import subprocess

def download_file(url, filename):
    r = requests.get(url)
    with open(filename, "wb") as f:
        f.write(r.content)
    return filename

def create_video(text):
    image = download_file("https://picsum.photos/720/1280", "image.jpg")
    audio = download_file("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", "audio.mp3")

    safe_text = text.replace(":", "\\:").replace("'", "\\'").replace("\n", " ")

    output = "reel.mp4"

    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image,
        "-i", audio,
        "-t", "10",
        "-vf",
        f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='{safe_text}':fontcolor=white:fontsize=40:x=(w-text_w)/2:y=(h-text_h)/2",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-shortest",
        output
    ]

    subprocess.run(cmd, check=True)

    return output

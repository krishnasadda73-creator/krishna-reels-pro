import subprocess
import random
from pathlib import Path

IMAGE_DIR = Path("assets/images")
BGM_DIR = Path("assets/bgm")

def get_random_file(folder):
    files = list(folder.glob("*"))
    return str(random.choice(files))

def create_video(text):
    image = get_random_file(IMAGE_DIR)
    audio = get_random_file(BGM_DIR)

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

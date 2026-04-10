from moviepy.editor import *
import random
import os

def create_video(text):
    image = "https://picsum.photos/720/1280"
    audio = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

    clip = ImageClip(image).set_duration(10)

    txt = TextClip(text, fontsize=50, color='white', method='caption', size=(720,1280))
    txt = txt.set_position("center").set_duration(10)

    video = CompositeVideoClip([clip, txt])

    video.write_videofile("reel.mp4", fps=24)

    return "reel.mp4"

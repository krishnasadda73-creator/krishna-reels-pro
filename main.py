from text_generator import generate_text
from video_creator import create_video

def main():
    text = generate_text()
    video = create_video(text)
    print("Done:", video)

if __name__ == "__main__":
    main()

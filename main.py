from text_generator import generate_text
from video_creator import create_video

def main():
    print("Starting pipeline...")

    text = generate_text()
    print("Generated Text:", text)

    video = create_video(text)
    print("Video created:", video)

if __name__ == "__main__":
    main()

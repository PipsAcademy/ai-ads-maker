import os
import sys
from openai import OpenAI
from moviepy.editor import ColorClip, AudioFileClip

# API Key Check
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY nahi mili. Settings > Secrets mein check karein.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def start_making():
    try:
        print("--- Step 1: Voiceover generating... ---")
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input="Welcome to your automated AI advertisement. Making videos daily with GitHub Actions."
        )
        response.stream_to_file("voice.mp3")
        print("Voice saved successfully!")

        print("--- Step 2: Creating Video... ---")
        audio = AudioFileClip("voice.mp3")
        
        # Simple Blue Background
        clip = ColorClip(size=(720, 1280), color=(0, 100, 255)).set_duration(audio.duration)
        
        video = clip.set_audio(audio)
        # fps=24 aur audio_codec lazmi hai GitHub par
        video.write_videofile("daily_ad.mp4", fps=24, codec="libx264", audio_codec="aac")
        
        print("--- SUCCESS: Video is ready! ---")

    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    start_making()

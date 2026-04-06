import os
from openai import OpenAI
from moviepy.editor import ColorClip, AudioFileClip

# API Setup
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def start_making():
    try:
        print("Step 1: AI Voice ban rahi hai...")
        # Simple Voiceover
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input="This is your daily AI generated advertisement. Innovation at its best."
        )
        response.stream_to_file("voice.mp3")

        print("Step 2: Video assemble ho rahi hai...")
        audio = AudioFileClip("voice.mp3")
        
        # Simple Blue Background (No images needed)
        clip = ColorClip(size=(720, 1280), color=(0, 100, 200)).set_duration(audio.duration)
        
        video = clip.set_audio(audio)
        video.write_videofile("daily_ad.mp4", fps=24, codec="libx264", audio_codec="aac")
        print("Mubarak ho! Video tayyar hai.")
        
    except Exception as e:
        print(f"Galti hui hai: {e}")
        exit(1) # Taake GitHub ko pata chale ke error hai

if __name__ == "__main__":
    start_making()

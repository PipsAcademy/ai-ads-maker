import os
from openai import OpenAI
from moviepy.editor import ColorClip, AudioFileClip

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Script aur Voiceover
response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="This is a daily AI generated ad. High quality products for you."
)
response.stream_to_file("voice.mp3")

# 2. Simple Video Assembly
audio = AudioFileClip("voice.mp3")
clip = ColorClip(size=(720, 1280), color=(0, 150, 255)).set_duration(audio.duration)
video = clip.set_audio(audio)
video.write_videofile("daily_ad.mp4", fps=24)

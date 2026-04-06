import os
from openai import OpenAI
from moviepy.editor import ColorClip, TextClip, AudioFileClip, CompositeVideoClip

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def start_making():
    # 1. Script Likhna
    print("AI Script likh raha hai...")
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Write a 20-second catchy ad script for a new sneaker."}]
    )
    script_text = res.choices[0].message.content

    # 2. Awaz Banana (TTS)
    print("AI Awaz bana raha hai...")
    audio_file = "voice.mp3"
    response = client.audio.speech.create(model="tts-1", voice="onyx", input=script_text)
    response.stream_to_file(audio_file)

    # 3. Video Banana (Simple Background + Audio)
    print("Video assemble ho rahi hai...")
    audio = AudioFileClip(audio_file)
    
    # Ek simple black background (Blue color)
    bg = ColorClip(size=(1080, 1920), color=(0, 102, 204)).set_duration(audio.duration)
    
    video = bg.set_audio(audio)
    video.write_videofile("daily_ad.mp4", fps=24, codec="libx264")
    print("Done!")

if __name__ == "__main__":
    start_making()

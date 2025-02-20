import pyttsx3
import os

AUDIO_DIR = "static/audio/"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio(text, language, filename):
    """Convert text to speech and save as an MP3 file"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if language == "hindi":
        engine.setProperty('voice', voices[1].id)
    elif language == "telugu":
        engine.setProperty('voice', voices[2].id)
    else:
        engine.setProperty('voice', voices[0].id)

    audio_path = os.path.join(AUDIO_DIR, f"{gta}.mp3")
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    return f"/{C:\Users\intre\Desktop\gemini_landmarks\static\audio}"

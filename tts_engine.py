import pyttsx3
from gtts import gTTS
import os

def speak_offline(text, rate=150, volume=1.0):
    """
    Offline TTS using pyttsx3
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    engine.say(text)
    engine.runAndWait()

def save_mp3(text, output_path):
    """
    Save speech as MP3 using gTTS
    """
    tts = gTTS(text)
    tts.save(output_path)

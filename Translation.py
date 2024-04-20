from fnmatch import translate
from time import sleep
from googletrans import Translator
import googletrans #pip install googletrans
from gtts import gTTS
import googletrans
import pyttsx3
import speech_recognition 
import os
import time
import playsound  # Adjusted import statement

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def translategl(query):
    speak("SURE SIR")
    print(googletrans.LANGUAGES)
    translator = Translator()
    speak("Choose the language in which you want to translate")
    to_lang = takeCommand().lower()  # Get language input through speech

    # Check if the language is valid
    if to_lang in googletrans.LANGUAGES:
        text_to_translate = translator.translate(query, src="auto", dest=to_lang)
        translated_text = text_to_translate.text

        try:
            speakgl = gTTS(text=translated_text, lang=to_lang, slow=False)
            speakgl.save("voice.mp3")
            playsound.playsound("voice.mp3")  # Adjusted playsound call
            time.sleep(5)
            os.remove("voice.mp3")
        except Exception as e:
            print("Unable to translate:", e)
    else:
        print("Invalid language selected")

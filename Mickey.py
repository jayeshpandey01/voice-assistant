import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import bs4
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 4
        r.energy_threshold = 200
        audio = r.listen(source,0,3)

    try:
        print("Understanding....")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            flag = True
            while flag:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    exit()

                elif "open" in query:
                    from file_open import openappweb
                    openappweb(query)
                elif "close" in query:
                    from file_open import closeappweb
                    closeappweb(query)

                elif "hello" in query:
                    speak("Ok sir, how are you?")
                elif "i am fine" in query:
                    speak("That great sir")
                elif "how are you" in query:
                    speak("perfect, sir")
                elif "thanks" in query:
                    speak("you are welcome, sir")
                elif "who created mickey" in query:
                    speak("Jayesh sir")

                elif "google"or "Google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query) # search on google

                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query) # Search on youtube
                    
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query) # wikipedia search

                elif "instagram" in query:
                    from searchNow import searchInstagram
                    searchInstagram(query) #instagram search

                elif "temperature" in query:
                    url = f"https://www.google.com/search?q={query}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{query} is {temp}")

                elif "weather" in query:
                    url = f"https://www.google.com/search?q={query}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{query} is {temp}")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                
                elif "who" or "what" or "why" or "where" in query:
                    from searchNow import searchonGoogle
                    searchonGoogle(query)

                
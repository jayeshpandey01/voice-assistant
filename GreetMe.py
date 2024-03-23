import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    current_time = datetime.datetime.now()
    current_minute = current_time.minute
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning,sir")
        speak(f"It's, {hour}:{current_minute}, How can i help you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ,sir")
        speak(f"It's, {hour} {current_minute}, How can i help you")

    else:
        speak("Good Evening,sir")
        speak(f"It's, {hour} {current_minute}, How can i help you")

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # If the query is ambiguous, provide options to the user
        options = ", ".join(e.options)
        return f"There are multiple options for '{query}'. Can you please specify? Options are: {options}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that topic."

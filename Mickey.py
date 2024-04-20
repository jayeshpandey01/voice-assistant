import random
import pyttsx3
import speech_recognition 
import webbrowser
import os
import datetime
import requests
from bs4 import BeautifulSoup
from plyer import notification
from pygame import mixer
import pyautogui
import speedtest
# import signal



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
        print("Understanding.....")
        query  = r.recognize_google(audio,language='en-in')
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

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break 
                elif "translate" in query:
                        
                    from Translator import translategl
                    query = query.replace("Mickey","")
                    query = query.replace("translate","")
                    translategl(query)
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)
                
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "play a game" in query:
                    from game import game_play
                    game_play()
                
                
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    
                elif "alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    # alarm(a)  # Remove this line
                    speak("Done,sir")
                elif "screenshot" in query:
                    import pyautogui #pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                        
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Mickey","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("Mickey","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/3B906pAxvdE?si=txCwAMDIQyVLEvjM")
                    elif b==2:
                        webbrowser.open("https://youtu.be/0-OY5w20E10?si=Qx5WvtUGoZKoGpFu")
                    elif b==3:
                        webbrowser.open("https://youtu.be/CAJDDTxlDp0?si=Klxt__bDaWWkKnZh")
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("Mickey","")
                    Calc(query)
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")
                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                elif "internet speed" in query:
                        wifi  = speedtest.Speedtest()
                        upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                        download_net = wifi.download()/1048576
                        print("Wifi Upload Speed is", upload_net)
                        print("Wifi download speed is ",download_net)
                        speak(f"Wifi download speed is {download_net}")
                        speak(f"Wifi Upload speed is {upload_net}")
                elif "ipl score" in query or "IPL" in query:
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")
                    team_elements = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")

                    if len(team_elements) >= 2:
                        team1 = team_elements[0].get_text()
                        team2 = team_elements[1].get_text()
                        team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
                        team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

                        print(f"{team1}: {team1_score}")
                        print(f"{team2}: {team2_score}")

                        notification.notify(
                            title="IPL SCORE:",
                            message=f"{team1}: {team1_score}\n{team2}: {team2_score}",
                            timeout=15
                        )
                    else:
                        print("Unable to fetch IPL score. Check the website structure or try again later.")

                
                
                elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("D:\\Coding\\Youtube\\Mickey\\FocusMode.py")
                        exit()

                            
                    else:
                        pass
                        
                elif "show my focus" in query:
                    from FocusGraph import focus_graph
                    focus_graph()
                    
                
                
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                        for i in range(3):
                            a = input("Enter Password to open Mickey :- ")
                            pw_file = open("password.txt","r")
                            pw = pw_file.read()
                            pw_file.close()
                            if (a==pw):
                                print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
                                break
                            elif (i==2 and a!=pw):
                                exit()

                            elif (a!=pw):
                                print("Try Again")
                    
                            elif shutdown == "no":
                                break
                        

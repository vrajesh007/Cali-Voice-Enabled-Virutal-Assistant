# pip install SpeechRecognition
#need to install all these packages first
import speech_recognition as sr #converts speech to text
import pyttsx3 #converts text to speech
import datetime #provides actual date and time
import wikipedia #searches anything on wikipedia
import webbrowser #provides interface for displayng web-based documents
import os # os related functionality
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('Loading your AI personal assistant - Cali')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
new_VoiceRate = 185
engine.setProperty('rate',new_VoiceRate)
engine.setProperty('voice', voices[1].id) #male voice
# engine.setProperty('voice','voices[0].id') #female voice


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hi,Good Morning")
        print("Hi,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hi,Good Afternoon")
        print("Hi,Good Afternoon")
    else:
        speak("Hi,Good Evening")
        print("Hi,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Getting input...")
        audio=r.listen(source)

        try:
            stmt=r.recognize_google(audio,language='en-in')
            print(f"user's statement:{stmt}\n")

        except Exception as e:
            speak("I can't hear you! please speak something")
            return "None"
        return stmt

speak("Loading your AI personal assistant cali")
wishMe()


if __name__=='__main__':


    while True:
        speak("Tell me how may I help you now?")
        stmt = takeCommand().lower()
        if stmt==0:
            continue

        if "good bye" in stmt or "okay bye" in stmt or "stop" in stmt:
            speak('Hope professor gives you an A. See you later, alligator')
            print('Your personal assistant Cali is shutting down,Good bye')
            break



        if 'wikipedia' in stmt:
            speak('Searching Wikipedia...')
            stmt =stmt.replace("wikipedia", "")
            results = wikipedia.summary(stmt, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in stmt:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in stmt:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in stmt:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in stmt:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in stmt:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in stmt or 'what can you do' in stmt:
            speak('I am Cali persoanl assistant. I am programmed to perform minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of LA and you can ask me computational or geographical questions too!')


        elif "who made you" in stmt or "who created you" in stmt or "who discovered you" in stmt:
            speak("I was built by Vrajesh")
            print("I was built by Vrajesh")

        elif "open stackoverflow" in stmt:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in stmt:
            news = webbrowser.open_new_tab("https://www.latimes.com/")
            speak('Here are some headlines from the LA times, Happy reading')
            time.sleep(6)

        elif "camera" in stmt or "take a photo" in stmt:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in stmt:
            stmt = stmt.replace("search", "")
            webbrowser.open_new_tab(stmt)
            time.sleep(5)

        elif 'ask' in stmt:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="JJRW6X-3TGUXLG4L4"
            client = wolframalpha.Client('JJRW6X-3TGUXLG4L4')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in stmt or "sign out" in stmt:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
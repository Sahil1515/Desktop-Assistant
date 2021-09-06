

import wolframalpha
from twilio.rest import Client
import requests
import time
import pyjokes
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import subprocess
from gtts import gTTS
# import mpyg321

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
assname='Paul'

def speak(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    # os.system("mpg321 welcome.mp3")
    os.system("play " + "welcome.mp3")


def WishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good morning sir!")
    elif hour > 12 and hour < 18:
        speak("Good aftenoon sir!")
    else:
        speak("Good evening sir!")

    speak("Paul here!")
    # speak("I am here for your help!")

# speak("Hi there! how are you?")


def takeCommand1():
    query1 = None
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        # r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query1 = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print(e)
        print("Unable to recognize")

    return query1

def takeCommand():
    query1=takeCommand1()

    while query1 ==None:
        query1=takeCommand1()
    
    return query1


if __name__ == '__main__':

    os.system('clear')
    WishMe()

    while True:
        query = None
        query = takeCommand()

        if query == None:
            continue

        print(query)
        query = query.lower()

        if 'wikipedia' in query.lower():
            speak("Searching wikipedia...")
            print("Searching wikipedia")
            # query=query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("http://youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("http://google.com/")
        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("http://stackoverflow.com")
        elif 'open code' in query:
            speak("Here you go to V S Code.Happy coding")
            os.system('code .')
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Sahil.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)


        elif "don't listen" in query or "stop listening" in query:
            speak("for how many seconds you want to stop Paul from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")

        # elif "camera" in query or "take a photo" in query:
        #     ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            # while snfm== None:
            #     snfm=takeCommand()

            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

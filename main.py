import speech_recognition as sr  # Module for converting voice to text (sr=module/another python file you can say)

# source=sr.Microphone() create object that handle on/active microphone
# r=sr.Recognizer() create object that has fxns useful of mention below
# r.adjust_for_ambient_noise(source) this fxn remove background voices
# audio=r.listen(source) this fxn listen from microphone and give audio
# text=r.recognize_google(audio) this fxn convert audio to text

import webbrowser  # helps to open internet things

# webrowser.open(link) open tab
import pyttsx3  # convert text to voice

# feature:offline
# pyttsx3 return engine object this engine conatin fxn
# engine.say(text) fxn accept text and using speaker sound produce
# imp engine.runAndWait() is necessayr

import random
import requests

# works with api help in fetching data using api-key and url
from musci_library import musci

# from gtts import gTTS more powerful text to speech module
import pygame


api = "006ad92811f6462f84a2d2294a39dce2"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api}"


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"{mode} Listening...")
            r.adjust_for_ambient_noise(
                source
            )  # <- This should be called BEFORE listening
            audio = r.listen(source)
        return r.recognize_google(audio)

    except Exception as e:
        print("Buffer!!", e)
        return "bakwass"


def start_song(c):
    if "back" in c:
        speak("Leaving song mode")
        return "default"

    for title in musci:
        if title in c:
            webbrowser.open(musci[title])
            return "music"
    speak("no such song is available")
    return "music"


def start_website(c):
    if "google" in c:
        webbrowser.open("https://google.com")
    elif "facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif "back" in c:
        speak("leaving website mode")
        return "default"
    else:
        speak("no such website available")
    return "website"


def start_news(c):
    if "back" in c:
        speak("leaving news mode")
        return "default"
    elif "news" in c:
        try:
            response = requests.get(url)
            data = (
                response.json()
            )  # after applying .json we get human readable text data/dict
            articles = data.get("articles", [])
            ran = random.randint(0, len(articles) - 1)
            dict1 = articles[ran]
            print(dict1["title"])
        except Exception as e:
            print("server error:")

    return "news"


# main loop
speak("Initializing Jarvis")
mode = "default"
while True:
    if mode == "default":
        command = listen().lower()
        if "jarvis" in command:
            speak("yes sir")
            command = listen().lower()
            if "song" in command:
                speak("initiating song mode")
                mode = "music"
            elif "website" in command:
                speak("initiating website mode")
                mode = "website"
            elif "news" in command:
                speak("Entering news mode")
                mode = "news"

    elif mode == "music":
        command = listen().lower()
        mode = start_song(command)
    elif mode == "website":
        command = listen().lower()
        mode = start_website(command)
    elif mode == "news":
        command = listen().lower()
        mode = start_news(command)

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing Tono")

Master = "Tuan"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# berbicara
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("halo good morning")  # dia akan ngomong selamat pagi 
    elif hour >= 12 and hour < 18:
        speak("halo selamat sore")
    else:
        print("halo selamat malam")
        speak("")

# mikropon
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan....")
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please")
        query = None

    return query

# program nyaa dimulai disini
wishMe()
speak("nama saya tono, ada yang bisa saya bantu"+Master)
query = takeCommand()

# logika untuk tugas sesuai permintaan
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif "open YouTube" in query.lower():
    url = "youtube.com"
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
elif "open Google" in query.lower():
    url = "google.com"
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!!")

    else:
        speak("Good evening!")

    speak("I am Jarvis Sir, Please tell me how may I help you")


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, 1)
        #r.energy_threshold = 800
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)

        print("say that again please.......")
        return "None"

    return query


if __name__ == "__main__":
    wishme()
    while True:
        # if 1:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open youtube' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'F:\Web Developing\Iron man Jarvis\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime}")

        elif 'open vs' in query:
            codePath = "C:\\Users\\acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'joke' in query:
            random_joke = pyjokes.get_joke()
            print(random_joke)
            speak(random_joke)

        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('screenshot taken')

        elif 'search' in query:
            speak("What do you want me to search for(plese type)?")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.open(search_url)
            speak(f"here is the results for the search term: {search_term}")

        elif 'bye' in query:
            speak("See you later")
            exit()

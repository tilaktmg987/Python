import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer=sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__== "__main__":
    speak("Initializing Rohan.....")

    while True:
        #listen for the wake word "rohan"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="rohan"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Rohan Active...")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                

                    processCommand(command)
        except Exception as e:
            print(" error; {0}".format(e))

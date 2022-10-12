import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("I am Jarvis AI Sir. how may I help you")        

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again Please")    
        return None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youmail@gmail.com', to ,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic for executing task based on query

        if 'wikipedia' in query:
            speak('Searching from Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")
        elif 'open Google' in query:
            webbrowser.get('chrome').open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")
        elif 'open facebook' in query:
            webbrowser.get('chrome').open("facebook.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
 
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strtime}")

        # elif 'open code' in query:
        #     codepath =  "C:\Users\Admin\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        #     os.startfile(codepath)
        elif 'email to chirag' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Chirag. I am not able to send email at this moment")        
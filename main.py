import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


print('''''
_______________________________________________________
 __      __       .__                               
/  \    /  \ ____ |  |   ____  ____   _____   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/ 
_______________________________________________________
''')


FILE = 'Niko' #Name des Freundes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#String Funktion wird dem eingegebenen String sprechen
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Diese Funktion sagt mir die Uhr
def wishMe():
    hour = datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak(f'Good morning {FILE}, its {hour} O´clock')
    elif hour>=12 and hour<18:
        speak(f'Good afternoon {FILE}, its {hour} O´clock')
    else:
        speak(f'Good Evening {FILE}, its {hour} O´clock')
    speak('How may I help you today?')


#Diese Funktione nimmt die requests entgegen und beantwortet sie
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        said = ""

    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        said = print(f'{FILE} said: {query}\n')
    except Exception as e:
        print('Say that again please')
        query = None
    return query



def main():
    #Main Programm startet hier:
    speak('Initializing Talib...')
    wishMe()
    query = takeCommand()

    #Logik fürs query suchen

    if 'wikipedia' in query.lower():
        speak('Searching in wikipedia')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower:
        webbrowser.open('youtube.com')

    elif 'play music' in query.lower:
        songs_dir = 'C:\\Users\\DELL-XR\\Videos\\4K Video Downloader'
        songs = os.listdir(songs_dir)
        print(songs)
        os.statfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'The time is {strTime}')
    else:
        print('KKK')
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
from random import randint
# import smtplib -> for send mail from gmail

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',rate-20)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening")
        speak("Good Evening")
    print("I am Ashutosh Patil Sir Assistance..How may I help You?")
    speak("I am Ashutosh Patil Sir Assistance..How may I help You?\n")
    print('For see the some number of command say "Help" \n')
    
import speech_recognition as sr
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as m:
        print("Listening ...")
        r.pause_threshold = 2
        audio = r.listen(m,phrase_time_limit=8)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query} \n")
    except Exception as e:
        #print(e)
        print("Please say that again \n")
        print("***************  HELP *************")
        print('For opening google say "Open Google" ')
        print('For opening youtube say "Open Youtube" ')
        print('For opening wilipedia say searching boject with wikipedia "Ex, Sachin Tendulkar wikipedia"')
        print('For exit say "Exit" ')
        print('For Play the song say "play song"')
        print('For check the current time and date say "what is time now"')
        print('For open VS code say "open vs code" ,and so on')
        print("etc...\n")
        return "None"
    return query

#This assistance also send mail but I disable or comment out it for some security reasons
'''
def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<Our Email Address>', '<password>')
    server.sendmail('<Our Email Address>', to, content)
    server.close()
    '''

if __name__ == "__main__":
    print("Namaste User")
    speak("Namaste User")
    wishme()
    while True:
        query = takecommand().lower()
        if 'exit' in query:
            exit()
        if 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'who created you' in query:
            print("Mr. Ashutosh Patil Sir created me")
            speak("Mr. Ashutosh Patil Sir created me")
        elif 'open youtube' in query:
            speak("Opening the youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening the google")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            speak("Opening the stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
            print("Opening the linkedin")
            speak("Opening the linkedin")
            print("You can connect Ashutosh Patil sir on linkedin. 'Link - https://www.linkedin.com/in/ashutosh-patil-16964b17a/'")
            speak("You can connect Ashutosh Patil sir on linkedin. 'Link - https://www.linkedin.com/in/ashutosh-patil-16964b17a/'")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("Opening the facebook")
        elif 'open instagram' in query:
            print("opening the Instgram")
            speak("opening the Instgram")
            webbrowser.open("instagram.com")
            print("You can follow Ashutosh Patil sir on Instagram username is ashutosh___patil")
            speak("You can follow Ashutosh Patil sir on Instagram username is ashutosh___patil")
        elif 'help' in query:
            print("***************  HELP *************")
            print('For opening google say "Open Google" ')
            print('For opening youtube say "Open Youtube" ')
            print('For opening wilipedia say searching boject with wikipedia "Ex, Sachin Tendulkar wikipedia"')
            print('For exit say "Exit" ')
            print('For Play the song say "play song"')
            print('For check the current time and date say "what is time now"')
            print('For open VS code say "open vs code" ,and so on')
            print("etc...\n")
        elif 'play song' in query:
            music_dir = 'F:\\Music' #Here on this path I saved some songs on my computer
            value = randint(0,24)
            songs =os.listdir(music_dir)
            print(songs[value])
            os.startfile(os.path.join(music_dir, songs[value]))
        elif 'what is time now' in query:
            currTime = datetime.datetime.now().strftime("%H:%M:%S")
            currDate = datetime.datetime.now()
            yr = currDate.year
            week = currDate.strftime("%A")
            month = currDate.strftime("%B")
            day = currDate.strftime("%d")
            print(f"The time is {currTime}")
            speak(f"The time is {currTime}")
            print(f"Today's date is {day}-{month}-{yr}, {week}")
            speak(f"Todays date is {day} {month} {yr} {week}")
        elif 'open vs code' in query:
            vscode = "C:\\Users\\Ashutosh Patil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            print("Opening the VS code..")
            speak("Opening the vs code")
            os.startfile(vscode)
        elif 'open android studio' in query:
            andr = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            print("Opening the Android Studio..")
            speak("Opening the android studio")
            os.startfile(andr)
       
        #This assistance also send mail but I disable or comment out it for some security reasons
        '''
        elif 'email to ashutosh':
            try:
                print("I send mail to Ashutosh Sir")
                speak(I send mail to Ashutosh Sir)
                content = takecommand()
                to = "<Receiver Email Address>"
                sendmail(to, content)
                print("Email is on the way..This is for only testing dont spam on this email Please")
                speak("Email is on the way..This is for only testing dont spam on this email Please")
            except Exception as e:
                print(e)
                print("Sorry! I am not able to send mail. Something is wrong.")
                speak("Sorry! I am not able to send mail. Something is wrong.")
        '''
                
            
        
            
            
            
            
            
            
        
       
            
    

import pyttsx3
import winsound
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit
import sys
import pyautogui
import pyjokes
from requests import get #helps to get ip address of a system
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")) #setting chrome as our web browser
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):     # It speaks whatever text user writes
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    time=datetime.datetime.now().strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good morning! It's {time}")
        print(f"Good morning! It's {time}")
    elif hour>=12 and hour<18:
        speak(f"Good afternoon! It's {time}")
        print(f"Good afternoon! It's {time}")
    else:
        speak(f"Good evening! It's {time}")
        print(f"Good evening! It's {time}")
    speak("I am Jarvis sir. How may I help you?")
    print("I am Jarvis sir. How may I help you?")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()  #helps in recognizing audio
    with sr.Microphone() as source:
        print("Listening...")
        #r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1 #wait for 1sec before considering the phrase is complete
        try:
            audio=r.listen(source,timeout=10,phrase_time_limit=5)
        except Exception as e:
            print("Sir you have not said anything. I am waiting for your command. How may I help you?")
            speak("Sir you have not said anything. I am waiting for your command. How may I help you?")
            takeCommand()

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('bikram.singh294@gmail.com','singh@17101998')
    server.sendmail('bikram.singh294@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'set alarm' in query:
            #print("Tell me the hour to set alarm")
            #speak("Tell me the hour to set alarm")
            #hr=takeCommand()
            #print("Tell me the minute to set alarm")
            #speak("Tell me the minute to set alarm")
            #min=takeCommand()
            #print("Tell me if it's AM or PM")
            #speak("Tell me if it's AM or PM")
            #a_p=takeCommand().upper()
            print("Tell me the time to set alarm. Say it like, 'Set alarm to 5:30 pm'")
            speak("Tell me the time to set alarm. Say it like, 'Set alarm to 5:30 pm'")
            tt=takeCommand()
            tt=tt.replace("set alarm to ", "") #5:30 p.m.
            tt=tt.replace(".","") # 5:30 pm
            tt=tt.upper() #5:30 PM
            lst=tt.split(':') # lst=['5', '30 PM']
            lst2=lst[1].split() # lst2=['30', 'PM']
            print(f"Setting alarm to {tt}")
            speak(f"Setting alarm to {tt}")
            while True:
                if int(datetime.datetime.now().strftime("%I")) == int(lst[0]) and datetime.datetime.now().strftime("%p")==lst2[1]:
                    if int(datetime.datetime.now().strftime("%M")) == int(lst2[0]):
                        print("Alarm is running..")
                        winsound.PlaySound('abc',winsound.SND_LOOP)
                    elif int(lst2[0])<int(datetime.datetime.now().strftime("%M")):
                        break
                    
        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            print("Sir, what should i search on google?")
            speak("Sir, what should i search on google?")
            cmd=takeCommand().lower()
            webbrowser.get('chrome').open("https://google.com/search?q=%s" % cmd)

        elif 'open stackoverflow' in query:
            webbrowser.get('chrome').open("stackoverflow.com")

        elif 'open flipkart' in query:
            webbrowser.get('chrome').open("flipkart.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd)) #similar to os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
        
        elif 'open code' in query:
            codePath="C:\\Users\\Bikramdeep Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open adobe photoshop' in query:
            os.startfile("C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe")

        elif 'open notepad' in query:
            os.startfile("C:\\WINDOWS\\system32\\notepad.exe")

        elif 'open vlc' in query:
            os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

        elif 'open adobe illustrator' in query:
            os.startfile("C:\Program Files\Adobe\Adobe Illustrator CC 2019\Support Files\Contents\Windows\Illustrator.exe")

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open chrome' in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        elif 'play movies' in query:
            movie_dir = 'D:\\Movies'
            movies=os.listdir(movie_dir)
            print(movies)
            os.startfile(os.path.join(movie_dir,movies[random.randint(0,len(movies)-1)]))

        elif 'email to' in query:
            try:
                dict={'bikram':'bikramdeepsingh37@gmail.com', 'bro':'kawaljeet.bcm@gmail.com'}
                if query.split()[-1] in dict:
                    to=dict[query.split()[-1]]
                else: 
                    continue
                speak("What should I say?")
                content=takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry biki bro but email not send")

        elif 'ip address' in query:
            ip=get("https://api.ipify.org").text
            print(f"Your ip address is {ip}")
            speak(f"Your Ip address is {ip}")

        elif 'send message' in query:
            try:
                print("What message should i send?")
                speak("What message should i send?")
                msg=takeCommand()
                contact={'bro':'+917986564961', 'bipul':'+919361561628', 'chirag':'+918708164817', 'me':'+919877639553'}

                if query.split()[-1] in contact:
                    to=contact[query.split()[-1]]
                    print("Any file you wanna attach along with your message?")
                    speak("Any file you wanna attach along with your message?")
                    response=takeCommand().lower()
                    if response=='yup' or response=='yes':
                        speak("Enter path of the file")
                        path=input("Enter path of the file, 'enter it like: D:\\Images\\44849.jpg' \n")
                        pywhatkit.sendwhatmsg(to,msg,int(datetime.datetime.now().hour),int(datetime.datetime.now().minute)+2)
                        pywhatkit.send_file(to,path,int(datetime.datetime.now().hour),int(datetime.datetime.now().minute)+2)
                else:
                    continue
            except Exception as e:
                print("Sorry Biki bro but your message not send")
                speak("Sorry Biki bro but your message not send")

        elif 'close'in query:
                apps={'notepad':'notepad.exe', 'code':'code.exe', 'chrome':'chrome.exe','google':'chrome.exe','vlc':'vlc.exe', 'sublime':'sublime_text.exe', 'command':'cmd.exe'}
                if query.split()[1] in apps:
                    print(f"Okay sir, closing {query.split()[1]}...")
                    speak(f"Okay sir, closing {query.split()[1]}...")
                    os.system(f"taskkill /f /im {apps[query.split()[1]]}")
                    

        elif 'no thanks' in query:
            speak("Thanks for using me sir, have a good day ahead.")
            sys.exit()

        elif 'tell me a joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'turn off the system' in query:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'on youtube' in query:
            query=query.replace(" on youtube","")
            query=query.replace("play ","")
            webbrowser.get('chrome'),open('https://www.youtube.com/results?q=' + query )

        speak("Sir, do you have any other work for me?")
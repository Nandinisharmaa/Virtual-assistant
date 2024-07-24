# import requests
# response=requests.request("get","https://en.wikipedia.org/wiki",verify=False)#SSL verification 

import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import wikipedia

#import pywhatkit


t=datetime.datetime.now()#time
time=t.strftime("%H:%M:%S")
hour=t.hour
user="Boss"
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',160)
def wishMe():
    if (hour>0 and hour<12):
        engine.say(f"Good Morning {user} ")
    elif (hour>=12 and hour<16):
        engine.say(f"Good Afternoon {user}")
    elif (hour>=16 and hour<19):
        engine.say(f"Good Evening {user}")
    elif (hour>=19 and hour<23):
        engine.say(f"Good night {user}")
    else:
        engine.say(f"Good night {user}")
    engine.say("I am Siri! How may I help You")
wishMe()
engine.runAndWait()#infinite loop
def takecommand():# this function returns query in string format
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=0.5   #after this time gap the VA start answering
        r.energy_threshold=300  #noise cancellation
        audio=r.listen(source)
        print("Recognising.....")
        query=r.recognize_google(audio,language="en-in")
    return query
def speak(audio):#say function
    engine.say(audio) 
    engine.runAndWait()
#speak("Hi Gorakhpur")    
# 
#   
q=takecommand().lower()

print(f"Request: {q}")

if "facebook" in q:
    speak("facebook is opening")
    webbrowser.open("fb.com")
elif 'whatsapp' in q:
    speak("Whatsapp is opening")
    webbrowser.open("https://web.whatsapp.com/")
elif "wikipedia" in q:#Java on wilipedia
    q=q.replace("wikipedia","")
    result=wikipedia.summary(q,sentences=3)
    print(f"Response: {result}")
    speak(result)
elif 'time' in q:
    time=datetime.datetime.now().strftime("%H:%M")
    speak(f"time is {time}")
# elif "youtube" in q:
#     webbrowser.open("youtube.com",)
elif "google" in q:
    q=q.replace("google","")
    result=webbrowser.open("https://google.com/search?q="+q)
    speak(q)
elif (("song" in q) and ("local" in q)):
    music_dir="D:/entertainment/music" 
    songs=os.listdir(music_dir)
    rnd_song=random.choice(songs)
    # print(type(songs))
    # print(type(rnd_song))
    os.startfile(music_dir+"/"+rnd_song)
elif (("song" in q) or ("play" in q) or ("youtube" in q)):
    q=q.replace("song","")
    q=q.replace("play","")
    #speak(f"playing the song {q}")
    webbrowser.open("https://www.youtube.com/results?search_query="+q)

elif "time" in q:
    engine.say(f"time is {time}")
elif "sleep" in q:
    speak(f"thank you {user}. I am sleeping whenever you need me just call")
    #speak(f"thank you {user}. HAm sone jaa rahe haiin")
else:
    speak("Sorry! I am not trained in the particular topic. I will back to you when I will well known.")
#have to add check wheather









#os.startfile("D:\entertainment\salar.mkv")
# lis=[3,4,6,7]
# print(random.choice(lis))
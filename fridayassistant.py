import pyttsx3
import datetime
import speech_recognition as sr 
import webbrowser as wb
import os

friday = pyttsx3.init()
voice = friday.getProperty('voices')  #lay giong noi trong thu vien
friday.setProperty('voice',voice[1].id) #chon giong nu

def speak(audio):
    print('F.R.I.D.A.Y: ' + audio) 
    friday.say(audio)
    friday.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p") #i la gio, m la phut, p la pm hoac am
    speak("Now is " + Time)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning sir!")
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Goodnight sir!")
    speak('How can i help you??')

def command():
    c = sr.Recognizer()  #nhan giong noi
    with sr.Microphone() as source: #nghe tu nguon la audio
        c.pause_threshold=1         #dung 2s truoc khi nhan lenh moi
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Nguyen Minh: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query=str(input("Your order is: "))
    return query

if __name__ == "__main__":
    time()
    welcome()
    while True:
        query = command().lower()      #chuyen thanh dang khong viet hoa
        if "google" in query:
            speak("What should i search boss??")
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'Here is yours {search} on google')

        if "youtube" in query:
            speak("What should i search boss??")
            search=command().lower()
            url=f'https://www.youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'Here is yours {search} on youtube')
        elif "what time" in query:
            time()
        elif "quit" in query:
            speak("Friday is quitting sir. Goodbye boss")
            quit()
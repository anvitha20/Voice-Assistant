import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import subprocess
import wikipedia




def sptext():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        recognize.adjust_for_ambient_noise(source)             
        audio = recognize.listen(source)
        try:
            print("Recognizing......")
            data = recognize.recognize_google(audio)
            print(data)
            return(data)
        except sr.UnknownValueError:
            print("Not Understand")
def txtsp(x):
    engine = pyttsx3.init()
    v = engine.getProperty('voices')
    engine.setProperty('voice',v[1].id)
    r = engine.getProperty('rate')
    engine.setProperty('rate',125)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__' :
   clear = lambda: os.system('cls')
   clear()
   if "nova" in sptext().lower():
    print("Hello")
    txtsp('hello')
    print("How can I help you?...")
    txtsp('How can I help you?...')
    
    while(1):
      data1 = sptext().lower()
      if "time" in data1:
        time = datetime.datetime.now().strftime("%I:%M%p")
        txtsp(time)
      elif "date" in data1:
        date = datetime.datetime.now().strftime("%B %d")
        txtsp(date)
      elif "your name" in data1:
        name = 'My name is nova'
        txtsp(name)
      elif "youtube" in data1:
        txtsp('opening youtube')
        link = webbrowser.open("https://www.youtube.com/")
      elif "joke" in data1:
        joke = pyjokes.get_joke(language='en',category='neutral')
        print(joke)
        txtsp(joke)
      elif "google" in data1:
        txtsp('opening google')
        tab = webbrowser.open("https://www.google.com/")
      elif "calculator" in data1:
        txtsp('opening calculator')
        calci = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
      elif "exit" in data1:
        txtsp('Thank you')
        break; 
      elif "wikipedia" in data1:
          data1=data1.replace("wikipedia","")
          results = wikipedia.summary(data1,sentences = 3)
          txtsp('According to wikipedia')
          print(results)
          txtsp(results)
   else:
    print("thanks")
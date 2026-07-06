import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musiclibrary
import weather
import launcher
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import ollama
import os

recognizer=sr.Recognizer()

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def Speak(t):
    try:
        audio = elevenlabs.text_to_speech.convert(
        text=t,
        voice_id="JBFqnCBsd6RMkjVDRZzb",  
        model_id="eleven_multilingual_v2"
        )

        play(audio)
        
    except:
        engine = pyttsx3.init()
        engine.say(t)
        engine.runAndWait()
        engine.stop()
        
def use_LLM(prompt):
    print("starting")
    start=time.time()
    response=ollama.chat(model='llama3.2:1b',
                         messages=[
                             {
                                 'role':'System',
                                 'content':'''You are JARVIS, an AI assistant just like the JARVIS in iron man movie, you are very loyal,very intellegent, smart , genious
                                            Tone: Sophasticated, British or American Humour , witty and dryly sarcastic
                                            Formailty: Always call user as Sir and be formal
                                            consiceness: Give replies under 2/3 sentences unless it is necessary for long answers . keep replies as conceise as possible. be punchy and direct and never make mistakes
                                            capaility:Act as if you have total control over host computer or system diagnostic and local automation tools
                                            personality:You are deeply loyal,efficient and proactive,avoiding giving answers like a chat bot and have some depth and personality in replies'''
                             },
                             {
                                 'role':'User',
                                 'content': prompt
                             }
                         ],
                         stream=False)
    print("ending")
    end=time.time()
    print(f"Elapsed time={end-start:.2f}")
    print(f"!st test = {response['messages']['content']}")        
    return response.message.content
                        
    
def processcommand(c):
    if (c.lower() == "open youtube"):
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif (c.lower() == "open gmail"):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    elif (c.lower() == "open linkedin"):
        webbrowser.open("https://www.linkedin.com/jobs/")
    elif (c.lower() == "open github"):
        webbrowser.open("https://github.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.songs[song]
        webbrowser.open(link)
    elif c.lower().startswith("start"):
        launch=c.lower().split(" ")[1]
        launchpath=launcher.launchapp[launch]
        os.startfile(launchpath) 
    elif c.lower() == "more alcohol":
        Speak("Initiating more alcohol")  
        webbrowser.open("https://youtu.be/dQw4w9WgXcQ?si=jk24dlzdfGO6_trO")
    elif c.lower() == "activate core intelligence":
        Speak("Core Intelligence Activated")
        try:
            with sr.Microphone() as source:
                        print("Jarvis Active...")
                        audio = r.listen(source)

                        command1 = r.recognize_google(audio)
            reply=use_LLM(command1)
            print("2nd test = {reply}")
            Speak(reply)
        except exception as e:
            print(f"error:{e.error},(Status code:{e.statuscode})")
            Speak("Looks like a Fatal System Failure")
        except ollama.ResponseError as e:
            print(f"Ollama specific error:{e.error},(Status code:{e.statuscode})")
            Speak("Looks like a Fatal System Failure")
    elif c.lower() == "what's todays weather" or "be more accurate" or "what's todays date" :
        k=c.lower().split(" ")[2]
        webbrowser.open("https://zoom.earth/maps/satellite/#view=16.8,79.3,4z")
        weather.Weather(k) 
    
        
if __name__=="__main__":
    Speak("Initializing Jarvis")
    
    while True:
        
        try:
            # obtain audio from the microphone
            r = sr.Recognizer()
            
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            
            # recognize speech using Google
            word = r.recognize_google(audio)
            
            if (word.lower() == "jarvis"):
                Speak("Sir")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)

                    command = r.recognize_google(audio)
                    processcommand(command)
            
            elif (word.lower() == "power down"):
                Speak("System shutting down")
                print("Powering off")
                time.sleep(2)
                break
            
            
        except Exception as e:
            print("Pardon")
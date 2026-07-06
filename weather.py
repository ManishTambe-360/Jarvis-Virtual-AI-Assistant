from dotenv import load_dotenv
import os
import requests
import geocoder
import json
from datetime import datetime
from main import Speak
from elevenlabs.client import ElevenLabs

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def Weather(keyword):
    weather_api=os.getenv("Weather_API")
    g = geocoder.ip('me')
    lat=g.lat
    lon=g.lng
    try:
        response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_api}")
        if (response.status_code == 200):
            data=response.json()
            if keyword.lower() == "weather":
                Speak("Todays weather mainly seems like")
                for w in data["weather"]:
                    Speak(f"{w['main']}")
                Speak("And to be precise currently it is like")
                for w in data["weather"]:
                    Speak(f"{w['description']}")
            elif keyword.lower() == "accurate":
                temp= round(data["main"]["temp"] - 273.15,2)
                feelslike=round(data["main"]["feels_like"] - 273.15,2)
                mintemp=round(data["main"]["temp_min"] - 273.15,2)
                maxtemp=round(data["main"]["temp_max"] - 273.15,2)
                atmprs=round(data["main"]["pressure"]/ 1013.25,2)
                seaatm=round(data["main"]["sea_level"]/ 1013.25,2)
                grdatm=round(data["main"]["grnd_level"]/ 1013.25,2)
                visibility=data["visibility"]//1000
                wspeed=round(data["wind"]["speed"]*2.23,2)
                gspeed=round(data["wind"]["gust"]*2.23,2)
                Speak("To be more accurate")
                Speak(f"Temperature is {temp}degree celcius but it feels like{feelslike}degree celcius   Minimum Temperature is {mintemp}degree celcius   Maximum Temperature is {maxtemp}degree celcius")
                Speak(f"pressure is {atmprs}atmosphere    pressure at sea level is{seaatm}atmosphere    Pressure at ground level is {grdatm}atmosphere   Humidity is {data["main"]["humidity"]}percent in air")
                Speak(f"Visibility is {visibility}kilometers")
                Speak(f"Wind speed is {wspeed}miles per hour and sudden strong bust of wind that is gust is{gspeed}miles per hour")
                if(data["wind"]["deg"] == 0 or data["wind"]["deg"] == 360):
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from North ")
                elif 0<data["wind"]["deg"]<90:
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from NorthEast ")
                elif(data["wind"]["deg"] == 90):
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from East ")
                elif 90<data["wind"]["deg"]<180:
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from SouthEast ")
                elif(data["wind"]["deg"] == 180):
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from South ")
                elif 180<data["wind"]["deg"]<270:
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from SouthWest ")
                elif(data["wind"]["deg"] == 270):
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from West ")
                elif 270<data["wind"]["deg"]<360:
                    Speak(f"wind is {data["wind"]["deg"]}degrees means it is coming from NorthWest ")
                Speak(f"Precentage of cloud in sky is {data["clouds"]["all"]}percent")
            
            elif keyword.lower()=="date":
                todaydate=data["dt"]
                timezone=data["timezone"]
                sunrise=data["sys"]["sunrise"]
                sunset=data["sys"]["sunset"]

                localtime=todaydate + timezone
                dt=datetime.fromtimestamp(localtime)
                readabledate=dt.strftime("%A, %d %B %Y") # %A=week %d=day 2 digit %B =month in words %Y =year

                localtime1=sunrise + timezone
                dt1=datetime.fromtimestamp(localtime1)
                readablesunrise=dt1.strftime("%I %M %p") # %I=hour 12 hr format %M=minutes %p=AM/PM

                localtime2=sunset + timezone
                dt2=datetime.fromtimestamp(localtime1)
                readablesunset=dt2.strftime("%I %M %p")

                hours=timezone // 3600
                minutes=(timezone % 3600) // 60

                Speak(f"Todays date is {readabledate}")
                if(data["dt"]<data["sys"]["sunrise"]):
                    Speak(f"Sunrise will happen at {readablesunrise}")
                elif(data["dt"]>data["sys"]["sunrise"]):
                    Speak(f"Sunrise happened at {readablesunrise}")
                if(data["dt"]<data["sys"]["sunset"]):
                    Speak(f"Sunset will happen at {readablesunset}")
                elif(data["dt"]>data["sys"]["sunset"]):
                    Speak(f"Sunset happened at {readablesunset}")
                    
                if(data["timezone"]>0):
                    Speak(f"Our timezone is {hours}hours and {minutes:02d}minutes ahead of UTC") #02d= pad with 0 for 2 decimal places and d mean integer(number)
                elif(data["timezone"]==0):
                    Speak("We are perfectly at UTC")
                elif(data["timezone"]<0):
                    Speak(f"Our timezone is {hours}hours and {minutes:02d}minutes behind of UTC")
            
        else:
            Speak("Error 401")
            
    except Exception as e:
        Speak("Seems like we lost our connection with weather sattelites today")
        

    
    
    

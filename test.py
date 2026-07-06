from datetime import datetime


print("Todays weather seems like")
for w in data["weather"][0]:
    print(w["main"])
print("And to be precise it is like")
for w in data["weather"][0]:
    print(w["description"])


temp= data["main"]["temp"] - 273.15
feelslike=data["main"]["feels_like"] - 273.15
mintemp=data["main"]["temp_min"] - 273.15
maxtemp=data["main"]["temp_max"] - 273.15
atmprs=data["main"]["pressure"]// 1013.25
seaatm=data["main"]["sea_level"]// 1013.25
grdatm=data["main"]["grnd_level"]// 1013.25
visibility=data["visibility"]//1000
wspeed=data["wind"]["speed"]*2.23
gspeed=data["wind"]["gust"]*2.23
print("To be more accurate")
print(f"Temperature is {temp}degree celcius but it feels like{feelslike}degree celcius   Minimum Temperature is {mintemp}degree celcius   Maximum Temperature is {maxtemp}degree celcius")
print(f"pressure is {atmprs}atmosphere    pressure at sea level is{seaatm}atmosphere    Pressure at ground level is {grdatm}atmosphere   Humidity is {data["main"]["humidity"]}percent in air")
print(f"Visibility is {visibility}")
print(f"Wind speed is {wspeed}miles per hour and sudden strong bust of wind that is gust is{gspeed}miles per hour")
if(data["wind"]["deg"] == 0 or data["wind"]["deg"] == 360):
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from North ")
elif 0<data["wind"]["deg"]<90:
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from NorthEast ")
elif(data["wind"]["deg"] == 90):
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from East ")
elif 90<data["wind"]["deg"]<180:
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from SouthEast ")
elif(data["wind"]["deg"] == 180):
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from South ")
elif 180<data["wind"]["deg"]<270:
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from SouthWest ")
elif(data["wind"]["deg"] == 270):
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from West ")
elif 270<data["wind"]["deg"]<360:
    print(f"wind is {data["wind"]["deg"]}degrees means it is coming from NorthWest ")
print(f"Precentage of cloud in sky is {data["clouds"]["all"]}percent")

todaydate=data["dt"]
timezone=data["timezone"]
sunrise=data["sys"]["sunrise"]
sunset=data["sys"]["sunset"]

localtime=todaydate + timezone
dt=datetime.fromtimestamp(localtime)
readabledate=dt.strftime("%A, %d %B %Y")

localtime1=sunrise + timezone
dt1=datetime.fromtimestamp(localtime1)
readablesunrise=dt1.strftime("%I %M %p")

localtime2=sunset + timezone
dt2=datetime.fromtimestamp(localtime1)
readablesunset=dt2.strftime("%I %M %p")

hours=timezone // 3600
minutes=(timezone % 3600) // 60

print(f"Todays date is {readabledate}")
if(data["dt"]<data["sys"]["sunrise"]):
    print(f"Sunrise will happen at {readablesunrise}")
elif(data["dt"]>data["sys"]["sunrise"]):
    print(f"Sunrise happened at {readablesunrise}")
if(data["dt"]<data["sys"]["sunset"]):
    print(f"Sunset will happen at {readablesunset}")
elif(data["dt"]>data["sys"]["sunset"]):
    print(f"Sunset happened at {readablesunset}")
    
if(data["timezone"]>0):
    print(f"Our timezone is {hours}hours and {minutes:02d}minutes ahead of UTC")
elif(data["timezone"]==0):
    print("We are perfectly at UTC")
elif(data["timezone"]<0):
    print(f"Our timezone is {hours}hours and {minutes:02d}minutes behind of UTC")
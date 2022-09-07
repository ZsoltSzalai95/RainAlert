import os

import requests
from twilio.rest import Client

OWM_Endpoint="https://api.openweathermap.org/data/2.5/onecall"
api_key = "994ef471fcf9844e079e357e59cbe6ea"

TWILIO_ACCOUNT_SID="YOURACCOUNT"
TWILIO_ACCOUNT_SID="YOURACCOUNT"
TWILIO_AUTH_TOKEN="YOURTOKEN"

YOUR_PHONE_NUMBER= ""


#Copenhagen parameters, Denmark
parameters={
    "lat": 55.676098,
    "lon": 12.568337,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response=requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False

for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain=True

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It is going to rain today. Remember to bring an umbrella! ☔",
        from_="+19362593268",
        to = YOUR_PHONE_NUMBER
    )

    print(message.status)

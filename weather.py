import requests
from tkinter import messagebox as msgbox

#Gets IP Address for geolocation via IP To Geolocation
ip_request = requests.get("https://api.ipify.org?format=json")
ip = ip_request.json()["ip"]

location_request = requests.get(f"http://ip-api.com/json/{ip}")

if location_request.status_code == 200:
    country = location_request.json()["country"]
    longitude = location_request.json()["lon"]
    latitude = location_request.json()["lat"]
    print("Successfully fetched location...")
    print(f"{country}, {latitude} latitude, {longitude} longitude")
else:
    msgbox.showerror("Request Error", f"An error occured while trying to fetch location.\nStatus Code: {location_request.status_code}")
    quit()

weather_request = requests.get("https://wttr.in/52.52,13.41?format=j1")

if weather_request.status_code == 200:
    print("Successfully fetched weather...")
    if country == "United States" or "Palau" or "Bahamas" or "Belize" or "Cayman Islands" or "Micronesia":
        temperature = f"{weather_request.json()["current_condition"][0]["temp_F"]} F°"
        temperature_feels_like = f"{weather_request.json()["current_condition"][0]["FeelsLikeF"]} F°"
        condition = weather_request.json()["current_condition"][0]["weatherDesc"][0]["value"]
        final = f"Temperature: {temperature}\nFeels like: {temperature_feels_like}\nCondition: {condition}"
        print(final)
    else:
        temperature = f"{weather_request.json()["current_condition"][0]["temp_C"]} C°"
        temperature_feels_like = f"{weather_request.json()["current_condition"][0]["FeelsLikeF"]} C°"
        condition = weather_request.json()["current_condition"][0]["weatherDesc"][0]["value"]
        final = f"Temperature: {temperature}\nFeels like: {temperature_feels_like}\nCondition: {condition}"
        print(final)
else:
    msgbox.showerror("Request Error", f"An error occured while trying to fetch weather.\nStatus Code: {weather_request.status_code}")
    quit()

msgbox.showinfo("Weather", f"{final}")
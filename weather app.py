import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(location):
    api_key = "52128cdc4f66686e9d37782a52dfe3a7"  # Replace with your OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    return response.json()

def display_weather():
    location = location_entry.get()
    if location:
        data = get_weather_data(location)
        if data["cod"] != "404":
            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            get_weather_label.config(text=f"City: {city}, {country}\nTemperature: {temp}°C\nWeather: {weather}\nWind Speed: {wind_speed} m/s")
        else:
            messagebox.showerror("Error", "City not found")
    else:
        messagebox.showerror("Error", "Please enter a location")

root = tk.Tk()
root.title("My Weather App")
root.geometry("300x300")

location_label = tk.Label(root, text="Enter location:", font=("Times New Roman",24))
location_label.pack()

location_entry = tk.Entry(root,font=("Times New Roman",16))
location_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
get_weather_button.place(y=75,x=110)

get_weather_label = tk.Label(root, font=("Times New Roman",16))
get_weather_label.place(y=110,x=60)

root.mainloop()
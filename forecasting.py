import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        show_weather(weather_data)
    else:
        messagebox.showerror("Error", "Failed to fetch weather data.")

def show_weather(weather_data):
    description = weather_data["weather"][0]["description"].capitalize()
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]

    result_text = f"Weather: {description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    result_label.config(text=result_text)

def get_weather_button_clicked():
    city_name = city_entry.get()
    if city_name:
        get_weather(city_name, api_key)
    else:
        messagebox.showinfo("Info", "Please enter a city name.")

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = "YOUR_API_KEY"

app = tk.Tk()
app.title("Weather Forecasting App")

# GUI Components
label = tk.Label(app, text="Enter City:")
label.pack(pady=10)

city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=10)

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_button_clicked)
get_weather_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

app.mainloop()

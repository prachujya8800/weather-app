import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

API_KEY = "15c5f191b1573942532f2dab263dda0a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] != 200:
        messagebox.showerror("Error", "City not found!")
        return

    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"].title()
    wind = data["wind"]["speed"]
    icon_code = data["weather"][0]["icon"]

    temp_label.config(text=f"Temperature: {temp} °C")
    weather_label.config(text=f"Condition: {weather}")
    wind_label.config(text=f"Wind Speed: {wind} m/s")

    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_response = requests.get(icon_url, stream=True)
    img = Image.open(icon_response.raw)
    img = img.resize((100, 100))
    icon = ImageTk.PhotoImage(img)

    icon_label.config(image=icon)
    icon_label.image = icon

# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Prachujya's Weather App")
root.geometry("500x700")
root.resizable(False, False)
root.configure(bg="#87CEEB")   # Sky blue
  # Sky blue
tk.Label(
    root,
    text="Weather Forecast",
    font=("Helvetica", 20, "bold"),
    bg="#87CEEB",
    fg="#003366"
).pack(pady=15)


city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

tk.Button(
    root,
    text="Get Weather",
    font=("Helvetica", 12, "bold"),
    bg="#003366",
    fg="black",
    activebackground="#0059b3",
    padx=20,
    pady=10,
    command=get_weather
).pack(pady=15)


icon_label = tk.Label(root)
icon_label.pack()

temp_label = tk.Label(root, font=("Arial", 14))
temp_label.pack(pady=5)

weather_label = tk.Label(root, font=("Arial", 14))
weather_label.pack(pady=5)

wind_label = tk.Label(root, font=("Arial", 14))
wind_label.pack(pady=5)

root.mainloop()
import geocoder
g = geocoder.ip('me')
city = g.city

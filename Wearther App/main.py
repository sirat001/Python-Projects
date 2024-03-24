import requests
from tkinter import *

API_KEY = "YLGE7RoISnHIUGABSAj7kBAVo7iheCQK"

url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/27905?apikey={API_KEY}&language=en-us&details=true&metric=true"

response = requests.get(url=url)

weather_data = response.json()

temperature = weather_data[0]["Temperature"].get("Value")

window = Tk()
window.geometry("500x500")
window.title("Temperature Widget")
temp_label = Label(window)
temp_label.config(text=f"The temperature is : {weather_data[0]["Temperature"].get("Value")}")
temp_label.pack()

window.mainloop()

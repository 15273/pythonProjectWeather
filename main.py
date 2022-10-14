import math

import requests
from tkinter import *

# https://pro.openweathermap.org/data/2.5/forecast/hourly?lat=32.329369&lon=34.856541&appid=cf0e3b5ac6b59776c53a516218cd002f
OWM_endPoint = "https://pro.openweathermap.org/data/2.5/forecast/climate?"
api_key = 'cf0e3b5ac6b59776c53a516218cd002f'

weather_slice = []
start_point = -4
end_point = 0
weather_data = ""
print(weather_data)
str_weather = ""
weather_params = {
    "hermon": {
        "lat": 33.317296,
        "lon": 35.803121,
        "appid": api_key
    },
    "netania": {
        "lat": 32.329369,
        "lon": 34.856541,
        "appid": api_key
    },
    "jerusalem": {
        "lat": 31.768318,
        "lon": 35.213711,
        "appid": api_key
    },
    "newyork": {
        "lat": 40.712776,
        "lon": -74.005974,
        "appid": api_key
    }
}


def next_time_weather():
    global start_point
    global end_point
    global str_weather
    global weather_slice
    if end_point + 4 >= len(weather_data["list"]):
        end_point = 0
        start_point = -4
    end_point += 4
    start_point += 4
    weather_slice = weather_data["list"][start_point:end_point]
    print(weather_slice)
    print(weather_slice[0]['weather'][0]['main'])
    # ['day']
    str_weather = ""
    for i in range(len(weather_slice)):
        print(weather_slice[i]['temp'])
        str_weather += "\nthe temp in netania is in the day " + str(
            math.floor(weather_slice[i]['temp']['day'] - 273.15)) + " celsius degris in morn: " + \
                       str(math.floor(weather_slice[i]["temp"]['morn'] - 273.15)) + "\n"
        str_weather += "is gon be " + weather_slice[i]['weather'][0]['main'] + " end it will be a " + \
                       weather_slice[i]['weather'][0]['description'] + "\n"

    canvas.itemconfig(text_mr, text=str_weather)


def get_api_list1():
    global OWM_endPoint
    global start_point
    global end_point
    global response
    global weather_data
    global weather_slice
    start_point = 0
    end_point = 4

    response = requests.get(OWM_endPoint, params=weather_params["hermon"])
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["list"][start_point:end_point]
    next_time_weather()


print(weather_data)


def get_api_list2():
    global OWM_endPoint
    global start_point
    global end_point
    global response
    global weather_data
    global weather_slice
    start_point = -4
    end_point = 0
    response = requests.get(OWM_endPoint, params=weather_params["netania"])
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["list"][start_point:end_point]
    next_time_weather()


def get_api_list3():
    global OWM_endPoint
    global start_point
    global end_point
    global response
    global weather_data
    global weather_slice
    start_point = -4
    end_point = 0
    response = requests.get(OWM_endPoint, params=weather_params["jerusalem"])
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["list"][start_point:end_point]
    next_time_weather()


def get_api_list4():
    global OWM_endPoint
    global start_point
    global end_point
    global response
    global weather_data
    global weather_slice
    start_point = -4
    end_point = 0

    response = requests.get(OWM_endPoint, params=weather_params["newyork"])
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["list"][start_point:end_point]
    next_time_weather()


print(str_weather)

window = Tk()

window.title("weather app")
window.config(padx=20, pady=20)

canvas = Canvas(height=405, width=610, bg="white")
weather_image = PhotoImage(file="23613146140_6edfea579f_k.png")

canvas.create_image(305, 202.5, image=weather_image)
canvas.grid(column=0, row=0, columnspan=5)
text_mr = canvas.create_text(275,
                             200,
                             width=500,
                             text=str_weather,
                             fill="white",
                             font=("Arial", 20, "italic"))

true_button = Button(text="next", highlightthickness=0, command=next_time_weather, bg="green")
true_button.grid(column=0, row=1)

hermon_button = Button(text="hermon mountain", highlightthickness=0, command=get_api_list1, bg="green")
hermon_button.grid(column=1, row=1)

jerusalem_button = Button(text="jerusalem", highlightthickness=0, command=get_api_list2, bg="green")
jerusalem_button.grid(column=2, row=1)

netania_button = Button(text="netania", highlightthickness=0, command=get_api_list3, bg="green")
netania_button.grid(column=3, row=1)

new_york_button = Button(text="new york", highlightthickness=0, command=get_api_list4, bg="green")
new_york_button.grid(column=4, row=1)
get_api_list1()
next_time_weather()

window.mainloop()


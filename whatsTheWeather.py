# Create a program that pulls data from OpenWeatherMap.org that prints out information about the current weather, such as the high, the low, and the amount of rain for wherever you live. Depending on how skilled you are, you can actually do some neat stuff with this project.
#
# Subgoals
#
#     Print out data for the next 5-7 days so you have a 5 day/week long forecast.
#
#     Print the data to another file that you can open up and view at, instead of viewing the information in the command line.
#
#     If you know html, write a file that you can print information to so that your project is more interesting. Here is an example of the results from what I threw together.
#
# Tips
#
#     APIs that are in Json are essentially lists and dictionaries. Remember that to reference something in a list, you must refer to it by what number element it is in the list, and to reference a key in a dictionary, you must refer to it by it's name.
#
#     Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your data in Fahrenheit.

import requests
import math

API_key = YOUR_API

city_name = input("Enter a city name for next five day forecast: ")

base_url = "http://api.openweathermap.org/data/2.5/forecast?"

final_url = base_url + "appid=" + API_key + "&q=" + city_name.lower() + "&units=metric"

weather_data = requests.get(final_url).json()

print("")

try:
    for day in weather_data['list'][::8]:
        print("{} celsius ({})".format(math.floor(day['main']['temp']), day['weather'][0]['main']))
except KeyError:
    print("No records for that city")

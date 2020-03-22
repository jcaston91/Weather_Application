'''
Name: Jontavius Caston
Date: 5/28/2019
Course: DSC510-T301 - Intro to Python Programming
Assignment: Assignment 12
Desc: This program's purpose is to ask the user for either a zip code or a city name. We will
      then display the weather for the requested city or zip code.
'''
import json
import requests
from pprint import pprint

while True:                                                                                                             #while statement that allows the program to run until the user is finished.
    choice = input('\nHello and welcome to the Weather Application type exit to quit or enter to continue.\n')
    if choice == "exit":                                                                                                #if statement that allows user to exit the program
        break
    else:
        location = input("Please enter a city name or zip code: \n")                                                    #location input that will be used to look up the forecast
        if (location.isdigit() == True):
            try:
                zip_code = location                                                                                     #try statement that haandles zipcodes
                URL = "http://api.openweathermap.org/data/2.5/weather?&APPID=7b7279fe78e99c0dd33982b7efeb4ead&zip="     #api URL that we will connect to and retrieve the information from
                r = requests.get(URL + zip_code)
                print('The connection to the Weather API succeeded!\n')                                                 #statement that lets you know if your process was successful
                weather_json = r.json()
                print(weather_json)
                weather_str = json.dumps(weather_json, indent=2)                                                        #json format to make it easier to view
                pprint('The name of the selected city and country is:')
                print(weather_json['name'] + ', ' + weather_json['sys']['country'])                                     #prints selected city and country
                pprint('The sky description for you selected location is:')
                print(weather_json['weather'][0]['description'])                                                        #prints sky condition
                pprint('The current temperature is:')
                print(weather_json['main']['temp'], 'Kelvins')                                                          #prints the temperature in kelvins
                pprint('The wind speed is:')
                print(weather_json['wind']['speed'], 'M/S')                                                             #prints the wind speed
                pprint('The cloud coverage is:')
                print(weather_json['clouds']['all'], '%')                                                               #prints the cloud coverage
                pprint('The humidity is:')
                print(weather_json['main']['humidity'], '%')                                                            #Prints the humidity
            except:
                print("The connection to the Weather API failed!\n")                                                    #statement that lets you know if your process failed
        else:
            try:
                city_name = location                                                                                    #try statement that haandles cities
                URL = "http://api.openweathermap.org/data/2.5/weather?&APPID=7b7279fe78e99c0dd33982b7efeb4ead&q="       #api URL that we will connect to and retrieve the information from
                r = requests.get(URL + city_name)
                print('The connection to the Weather API succeeded!\n')                                                 #statement that lets you know if your process was successful
                weather_json = r.json()
                weather_str = json.dumps(weather_json, indent=2)                                                        #json format to make it easier to view
                pprint('The name of the selected city and country is:')
                print(weather_json['name'] + ', ' + weather_json['sys']['country'])                                     #prints selected city and country
                pprint('The sky description for you selected location is:')
                print(weather_json['weather'][0]['description'])                                                        #prints sky condition
                pprint('The current temperature is:')
                print(weather_json['main']['temp'], 'Kelvins')                                                          #prints the temperature in kelvins
                pprint('The wind speed is:')
                print(weather_json['wind']['speed'], 'M/S')                                                             #prints the wind speed
                pprint('The cloud coverage is:')
                print(weather_json['clouds']['all'], '%')                                                               #prints the cloud coverage
                pprint('The humidity is:')
                print(weather_json['main']['humidity'], '%')                                                            #Prints the humidity

            except:
                print("The connection to the Weather API failed!\n")                                                    #statement that lets you know if your process failed

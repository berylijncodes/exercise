# Geocoding app

Create a small app that shows the name of the city for a given geolocation using the free [Geocoding API](https://openweathermap.org/api/geocoding-api). It will first check if the information is already stored in a local database, and if not, it will fetch it from the API and store it in the database. The app asks the user for a latitude and longitude through the terminal, and then displays all matching cities in the terminal together with their country code.


## Requirements

We are searching for robust, readable and tested code. We would also like to see a git history.

A starting point is provided for you, it uses a class-based approach, as that is what you will be working with when you join us.

Feel free to rename the classes or methods provided, and to add more classes or delete the classes provided. You can also improve the code provided. Add as many tests as you need.

We work a lot with APIs and databases, so we hope you have fun with the exercise!


### Terminal GUI

The app should ask for a latitude and a longitude on the terminal, then print all the cities found and their country code.

You are free to choose how to ask for the information and how to show the results.

➡️ A method `foo` is provided in the class `UserInterface`, as well as some tests showing how to test reading input and printing output to the terminal. You can delete the `foo` method and add your own methods.


### Database

* When receiving the latitude and longitude from the user input, search the database for both a longitude in the range (lon - 0.03, lon + 0.03) and a latitude in the range (lat - 0.03, lat + 0.03).

* If nothing is found in the database, fetch the information from the Geocoding API and store it in the database.

* You should store the latitude, the longitude, the name of the city and the country code for every city returned by the API call.

➡️ A class `Database` is provided with a `connect` method. Add more methods as you need them. The tests use an in-memory database. [You can read more about sqlite3 here](https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3).


### API

* You need **an OpenWeather API key:** The Geocoding API is free but needs a valid API key to allow responses. [Create an account](https://home.openweathermap.org/users/sign_up) at the OpenWeather site and copy your API key.

* Provide the latitude and longitude and your API key as described [in the docs](https://openweathermap.org/api/geocoding-api).

➡️ A class `Client` is provided

## Install

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```


## To test

```sh
python3 -m unittest discover
```


## To run

```sh
python3 runner.py
```

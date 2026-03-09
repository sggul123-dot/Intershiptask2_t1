# Intershiptask2_t1
# Geolocation Tracker using Python

## Project Title

Geolocation Tracker

## Description

The Geolocation Tracker is a Python program that retrieves the user's geographical location based on their IP address. The program uses an online API to fetch location details such as city, country, latitude, and longitude. It then displays the location on an interactive map.

This project demonstrates how Python can be used to interact with web APIs and visualize geographical data.

## Objectives

* Fetch user location using IP address
* Display geographical information
* Show the location on a map
* Gain experience using Python libraries and APIs

## Technologies Used

* Python 3
* requests library
* folium library
* IP Geolocation API

## Required Libraries

Install the required libraries using the following commands:

py -m pip install requests
py -m pip install folium

## How the Program Works

1. The program sends a request to an IP geolocation API.
2. The API returns the user's location data in JSON format.
3. Python extracts the latitude and longitude values.
4. A map is generated using the folium library.
5. The location is marked on the map and saved as an HTML file.

## How to Run the Project

1. Install Python on your computer.
2. Install required libraries.
3. Save the program file as `geolocation_tracker.py`.
4. Open Command Prompt or Terminal.
5. Run the program using:

py geolocation_tracker.py

6. The program will generate a file named `location_map.html`.

## Output

* Displays city and country in the terminal.
* Generates an HTML map showing the user's location.

## Example Output

City: Example City
Country: Example Country

A map file named **location_map.html** will open in the browser showing the location marker.

## Learning Outcomes

* Working with APIs in Python
* Using external libraries
* Handling JSON data
* Creating interactive maps

## Author

Intern Name: **_**Sapna Gul_________
Program: Python Internship


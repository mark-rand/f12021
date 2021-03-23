#!/usr/bin/env python3
import itertools as it

constructors = [
    {"name": "Mercedes",  "pts2020": 573, "price": 38},
    {"name": "Red Bull Racing Honda",  "pts2020": 319,  "price": 25.9},
    {"name": "McLaren Renault",  "pts2020": 202,  "price": 18.9},
    {"name": "Racing Point BWT Mercedes",  "pts2020": 195,  "price": 17.6},
    {"name": "Renault",  "pts2020": 181,  "price":  15.4},
    {"name": "Ferrari",  "pts2020": 131,  "price":  18.1},
    {"name": "AlphaTauri Honda",  "pts2020": 107,  "price":  12.7},
    {"name": "Alfa Romeo Racing Ferrari",  "pts2020": 8,  "price":  8.9},
    {"name": "Haas Ferrari",  "pts2020": 3,  "price":  6.1},
    {"name": "Williams Mercedes",  "pts2020": 0,  "price":  6.3}
]

drivers = [
    {'name': 'Kimi Räikkönen ', 'pts2020': '4', 'price': '9.6'},
    {'name': 'George Russell ', 'pts2020': '3', 'price': '6.2'},
    {'name': 'Antonio Giovinazzi ', 'pts2020': '4', 'price': '7.9'},
    {'name': 'Sebastian Vettel ', 'pts2020': '33', 'price': '16.2'},
    {'name': 'Lance Stroll ', 'pts2020': '75', 'price': '13.9'},
    {'name': 'Charles Leclerc ', 'pts2020': '98', 'price': '16.8'},
    {'name': 'Esteban Ocon ', 'pts2020': '62', 'price': '10.1'},
    {'name': 'Sergio Perez ', 'pts2020': '125', 'price': '18.4'},
    {'name': 'Daniel Ricciardo ', 'pts2020': '119', 'price': '17.3'},
    {'name': 'Carlos Sainz ', 'pts2020': '105', 'price': '14.4'},
    {'name': 'Lando Norris ', 'pts2020': '97', 'price': '13.1'},
    {'name': 'Max Verstappen ', 'pts2020': '214', 'price': '24.8'},
    {'name': 'Valtteri Bottas ', 'pts2020': '223', 'price': '23.6'},
    {'name': 'Lewis Hamilton ', 'pts2020': '347', 'price': '33.5'}
]


def sumTeam(constructorChoice, driversChoice):
    if len(driversChoice) != 5:
        return False
    price = constructors[constructorChoice]['price']
    points = constructors[constructorChoice]['pts2020']
    for driver in driversChoice:
        price = price + float(drivers[driver]['price'])
        points = points + int(drivers[driver]['pts2020'])
    return (price, points)


print(list(it.combinations(range(0,len(drivers)), 5)))
for constructor in range(0,len(constructors)):
    for driverChoices in it.combinations(range(0,len(drivers)), 5):
        team = sumTeam(constructor, driverChoices)
        if (team[0] <= 100):
            print(f'Constructor: {constructor}. Drivers {driverChoices}. Total Points {team[1]}')
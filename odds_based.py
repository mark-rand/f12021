#!/usr/bin/env python3
import itertools as it

constructors = [
    {"name": "Mercedes",  "predictedPoints": 60, "price": 38},
    {"name": "Red Bull Racing Honda",  "predictedPoints": 80,  "price": 25.9},
    {"name": "McLaren Renault",  "predictedPoints": 36,  "price": 18.9},
    {"name": "Racing Point BWT Mercedes",  "predictedPoints": 10,  "price": 17.6},
    {"name": "Renault",  "predictedPoints": 1.5,  "price":  15.4},
    {"name": "Ferrari",  "predictedPoints": 4.25,  "price":  18.1},
    {"name": "AlphaTauri Honda",  "predictedPoints": 12,  "price":  12.7},
    {"name": "Alfa Romeo Racing Ferrari",  "predictedPoints": 0.25,  "price":  8.9},
    {"name": "Haas Ferrari",  "predictedPoints": 0.25,  "price":  6.1},
    {"name": "Williams Mercedes",  "predictedPoints": 0.25,  "price":  6.3}
]

drivers = [
    {'id': '00', 'name': 'Mick Schumacher', 'predictedPoints': 0.125, 'price': 5.8},
    {'id': '01', 'name': 'Nicholas Latifi', 'predictedPoints': 0.125, 'price': 6.5},
    {'id': '02', 'name': 'Nikita Mazepin', 'predictedPoints': 0.125, 'price': 5.5},
    {'id': '03', 'name': 'Antonio Giovinazzi', 'predictedPoints': 0.125, 'price': 7.9},
    {'id': '04', 'name': 'Kimi Raikkonen', 'predictedPoints': 0.125, 'price': 9.6},
    {'id': '05', 'name': 'George Russell', 'predictedPoints': 0.125, 'price': 6.2},
    {'id': '06', 'name': 'Yuki Tsunoda', 'predictedPoints': 0.125, 'price': 8.8},
    {'id': '07', 'name': 'Carlos Sainz', 'predictedPoints': 0.25, 'price': 14.4},
    {'id': '08', 'name': 'Esteban Ocon', 'predictedPoints': 0.5, 'price': 10.1},
    {'id': '09', 'name': 'Fernando Alonso', 'predictedPoints': 1, 'price': 15.6},
    {'id': '10', 'name': 'Sebastian Vettel', 'predictedPoints': 2, 'price': 14.4},
    {'id': '11', 'name': 'Charles Leclerc', 'predictedPoints': 4, 'price': 16.8},
    {'id': '12', 'name': 'Lance Stroll', 'predictedPoints': 8, 'price': 13.9},
    {'id': '13', 'name': 'Pierre Gasly', 'predictedPoints': 12, 'price': 11.7},
    {'id': '14', 'name': 'Lando Norris', 'predictedPoints': 16, 'price': 13.1},
    {'id': '15', 'name': 'Daniel Ricciardo', 'predictedPoints': 20, 'price': 17.3},
    {'id': '16', 'name': 'Valtteri Bottas', 'predictedPoints': 24, 'price': 23.6},
    {'id': '17', 'name': 'Sergio Perez', 'predictedPoints': 30, 'price': 18.4},
    {'id': '18', 'name': 'Lewis Hamilton', 'predictedPoints': 36, 'price': 33.5},
    {'id': '19', 'name': 'Max Verstappen', 'predictedPoints': 50, 'price': 24.8}
]


def sumTeam(constructorChoice, driversChoice):
    if len(driversChoice) != 5:
        return False
    price = constructors[constructorChoice]['price']
    points = constructors[constructorChoice]['predictedPoints']
    for driver in driversChoice:
        price = price + float(drivers[driver]['price'])
        points = points + int(drivers[driver]['predictedPoints'])
    return (price, points)


print(list(it.combinations(range(0, len(drivers)), 5)))
for constructor in range(0, len(constructors)):
    for driverChoices in it.combinations(range(0, len(drivers)), 5):
        team = sumTeam(constructor, driverChoices)
        if (team[0] <= 100):
            print(
                f'Constructor: {constructors[constructor]["name"]}. Drivers {driverChoices}. Total Points {team[1]}')


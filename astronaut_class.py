class Astronaut:
    """Astronaut Class"""
    def __init__(self,name, status, flightHours):
        print("initializing name, status, and flight hours")
        self.__name = name
        self.__status = status
        self.__flightHours = flightHours

    def __str__(self):
        return '%s %s' % (self.__name, self.__status)

    @property
    def name(self):
        print("Getting name")
        return self.__name
    
    def __gt__(self, other):
        print("__gt__ called - self: %s, other: %s" % (self, other))
        return self.__flightHours > other.flightHours

    def __eq__(self,other):
        print("__eq__ called - self: %s, other: %s" % (self, other))
        return self.__flightHours == other.flightHours

    def __ge__(self,other):
        print("__ge__ called - self: %s, other: %s" % (self, other))
        return self.__flightHours >= other.flightHours

    @property
    def flightHours(self):
        print("Getting flight hours")
        return self.__flightHours

    @property
    def status(self):
        print("Getting status")
        return self.__status

import random
import csv

file = open('astronauts_cleaned.csv', 'r')
astronautsDict = csv.DictReader(file)

astronautList = []

for i in astronautsDict:
    astronautList.append(Astronaut(i['Name'], i['Status'], i['Space Flight (hr)']))

for i in astronautList:
    print(i)

print(random.choice(astronautList) > random.choice(astronautList))
print(random.choice(astronautList) >= random.choice(astronautList))
print(random.choice(astronautList) == random.choice(astronautList))
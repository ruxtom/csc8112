import json
import requests
import collections
import time


# Gets values from the API a specified number of times, waiting 5 seconds between each request
def floorSensors():
    maxFloors = 6
    i = 1
    while i <= maxFloors:
        url = requests.get("https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity/floor-"+str(i))
        info = json.loads(url.text)
        print("Entity sensors for floor " + str(i))
        determineSensorsByFloor(info)
        i+= 1

def entitySensors():
    url = requests.get("https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity")
    info = json.loads(url.text)
    determineAllSensors(info)


def determineAllSensors(info):
    hasValue = []
    if info is None:
        return
    for items in info["items"]:
        for feed in items["feed"]:
            for timeseries in feed["timeseries"]:
                if "latest" in timeseries:
                    name = feed["metric"]
                    hasValue.append(name)
    counter = collections.Counter(hasValue)
    print("All entity sensors:")
    print(counter)

def determineSensorsByFloor(info):
    hasValue = []
    if info is None:
        return
    for feed in info["feed"]:
        for timeseries in feed["timeseries"]:
            if "latest" in timeseries:
                name = feed["metric"]
                hasValue.append(name)
    counter = collections.Counter(hasValue)
    print(counter)


entitySensors()
floorSensors()


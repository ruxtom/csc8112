import json
import requests
import collections
import time


# Gets values from the API a specified number of times, waiting 5 seconds between each request
def main():
    maxFloors = 6
    i = 1
    while i <= maxFloors:
        url = requests.get("https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity/floor-"+str(i))
        info = json.loads(url.text)
        determineIfHasValue(info)
        i+= 1

def determineIfHasValue(info):
    hasValue = []
    if info is None:
        return
    for feed in info["feed"]:
        for timeseries in feed["timeseries"]:
            if "latest" in timeseries:
                # print(name)
                name = feed["metric"]
                hasValue.append(name)
    counter = collections.Counter(hasValue)
    print(counter)

main()

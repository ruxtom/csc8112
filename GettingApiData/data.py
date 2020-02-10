import json
import requests
import collections
import time

# Gets values from the API a specified number of times, waiting 5 seconds between each request
def main():
    totalIterations = int(input("How many times would you like to collect the data: "))
    if type(totalIterations) is not int:
        raise Exception("Invalid total iterations type")
    completedIterations = 0

    while completedIterations < totalIterations:
        url = requests.get("https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity/floor-1")
        info = json.loads(url.text)
        temperature(info)
        completedIterations += 1
        time.sleep(5)
        print("Iteration: ", completedIterations, "/", totalIterations)
        print("Time left: ", (totalIterations - completedIterations)*5, "s")


# Extracts the temperature values from the API information
def temperature(info):
    data = _data_extractor(info, "C3 HTG Pump Power")
    print(data)


# Loops through the info array, extracting the specified metric values
def _data_extractor(info, metric):
    sensors = []
    data = []
    if info is None:
        return
		
    for feed in info["feed"]:
        if feed["metric"] == metric:
            sensors.append(feed)

    for sensor in sensors:
        for timeseries in sensor["timeseries"]:
            value = timeseries["latest"]["value"]
            data.append(value)

    return data

main()

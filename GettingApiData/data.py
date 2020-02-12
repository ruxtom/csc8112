import json
import requests
import collections
import time
import json
from kafka import KafkaProducer
import data


# Gets values from the API a specified number of times, waiting 5 seconds between each request
def main():
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),bootstrap_servers=['ec2-18-207-191-122.compute-1.amazonaws.com:9092','ec2-3-81-136-58.compute-1.amazonaws.com:9092','ec2-54-196-123-115.compute-1.amazonaws.com:9092'])
    #totalIterations = int(input("How many times would you like to collect the data: "))
    #if type(totalIterations) is not int:
    #    raise Exception("Invalid total iterations type")
    completedIterations = 0

    #while completedIterations < totalIterations:
    url = requests.get("https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity/floor-1")
    info = json.loads(url.text)
    temperature(info)
    completedIterations += 1
    #time.sleep(5)
    #print("Iteration: ", completedIterations, "/", totalIterations)
    #print("Time left: ", (totalIterations - completedIterations)*5, "s")
    #send = {
    #    "data":json.dumps(temperature(info))
    #}
    #print(send)
    #producer.send('usb-data', send)
    #producer.close()
    print("After producer close")


# Extracts the temperature values from the API information
def temperature(info):
    data = _data_extractor(info, "Power")
    #print(data)
    return data


# Loops through the info array, extracting the specified metric values
def _data_extractor(info, metricWanted):
    sensors = []
    metrics = []
    data = []
    whole = []
    if info is None:
        return
        
    for feed in info["feed"]:
        metric = feed["metric"]
        if metricWanted in metric:
            if metric != "Power":
                if "Voltage" not in metric:
                    sensors.append(feed)
                    metrics.append(metric)

    for sensor in sensors:
        name = sensor["metric"]
        for timeseries in sensor["timeseries"]:
            if "latest" in timeseries:
                
                value = timeseries["latest"]["value"]
                whole.append(name +" " + str(value))
                
                data.append(value)

    print(whole)
    return data

main()

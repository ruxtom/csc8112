import json
import requests
import collections
import time
import json
from kafka import KafkaProducer

failedSensors = 0
# Gets values from the API a specified number of times, waiting 5 seconds between each request
def main():
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=['ec2-18-207-191-122.compute-1.amazonaws.com:9092',
                           'ec2-3-81-136-58.compute-1.amazonaws.com:9092',
                           'ec2-54-196-123-115.compute-1.amazonaws.com:9092']
    )
#totalIterations = int(input("How many times would you like to collect the data: "))
    #if type(totalIterations) is not int:
    #    raise Exception("Invalid total iterations type")
    completedIterations = 0

    #while completedIterations < totalIterations:
    #url = requests.get("https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity/floor-1")
    #url = requests.get('https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity?metric="room temperature"')
    i = 1
    for i in range(41):
        url = requests.get('https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity?metric="room temperature"&page='+str(i))
        info = json.loads(url.text)
        temperature(info)
        completedIterations += 1
    #time.sleep(5)
    #print("Iteration: ", completedIterations, "/", totalIterations)
    #print("Time left: ", (totalIterations - completedIterations)*5, "s")
        toSend = temperature(info)
        c = 0
        length = len(toSend)
        print("Sending data...")
        for c in range(length):
            send = {
                "data":json.dumps(toSend[c])
            }
            producer.send('usb', send)
            producer.flush()
    producer.close()
    print("Unusable sensors: " + str(failedSensors))

# Extracts the temperature values from the API information
def temperature(info):
    data = _data_extractor(info, "Temperature")
    #print(data)
    return data


# Loops through the info array, extracting the specified metric values
def _data_extractor(info, metricWanted):
    global failedSensors
    sensors = []
    metrics = []
    data = []
    whole = []
    if info is None:
        return
        
    for items in info["items"]:
        name = items["name"]
        for feed in items["feed"]:
            metric = feed["metric"]
            if metricWanted in metric:
                for timeseries in feed["timeseries"]:
                    if "latest" in timeseries:
                        try:
                            value = timeseries["latest"]["value"]
                        except:
                            failedSensors = failedSensors + 1
                            print("An Error in last timeseries")
                        try:
                            whole.append(name +" " + str(value))
                        except:
                            print("Can't append whole")
                #if metric != "Power":
                    #if "Voltage" not in metric:
                #sensors.append(feed)
                #metrics.append(metric)

    #for sensor in sensors:
    #    sType = sensor["metric"]
    #    name = sensor["name"]
    #    for timeseries in sensor["timeseries"]:
    #        if "latest" in timeseries:
    #            
    #            value = timeseries["latest"]["value"]
    #            whole.append(sType + " " + name +" " + str(value))
    #            
    #            data.append(value)
    #print(whole)
    return whole

main()

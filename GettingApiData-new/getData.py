import json
import jsonpath
import requests
from kafka import KafkaProducer


# Specify kafka server address, call getPage and get raw data from API
def send2cloud(metric):
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=['ec2-34-228-191-220.compute-1.amazonaws.com:9092',
                           'ec2-52-23-217-206.compute-1.amazonaws.com:9092',
                           'ec2-54-152-219-229.compute-1.amazonaws.com:9092']
    )
    page = getPage(metric)
    for i in range(1, page + 1):
        print("metric: " + metric + " - Sending data..." + "page:" + str(i))
        rawData(metric, producer, i)
    producer.close()


# Loops through the info array, extracting the specified metric values
def rawData(metric, producer, i):
    if metric == "room temperature":
        topic = "usb-tem"
    elif metric == "humidity":
        topic = "usb-hum"
    else:
        topic = "usb-CO2"
    url = requests.get(
        'https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity?metric="' + metric + '"&page=' + str(i))
    info = json.loads(url.text)
    data_id = jsonpath.jsonpath(info, '$[items].[entityId]')
    for i in range(len(data_id) + 1):
        data_room = jsonpath.jsonpath(info, '$[items][' + str(i) + '][name]')
        data_time = jsonpath.jsonpath(info, '$[items][' + str(i) + '].[time]')
        data_value = jsonpath.jsonpath(info, '$[items][' + str(i) + '].[value]')
        if (type(data_room) != bool) & (type(data_value) != bool):
            data_compose = {'room': data_room, metric: []}
            for data_time, data_value in zip(data_time, data_value):
                sub_time = data_time[0:10] + " " + data_time[11:19]
                data_compose[metric].append({sub_time: data_value})
                print(data_compose)
                producer.send(topic, data_compose)
                producer.flush()

                # Get the total number of pages of this metric from the pageCount parameter of the API,
                # and determine the number of loops when obtaining raw data.


def getPage(metric):
    url = requests.get(
        'https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity?metric="' + metric + '"&page=1')
    info = json.loads(url.text)
    data_page = jsonpath.jsonpath(info, '$..[pageCount]')
    return data_page[0]

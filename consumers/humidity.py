from kafka import KafkaConsumer
from graphing import createGraph
import json


def hum_consumer():
    xAxis = []
    yAxis = []
    consumer = KafkaConsumer('usb-hum',
                             bootstrap_servers=['ec2-34-228-191-220.compute-1.amazonaws.com:9092',
                                                'ec2-52-23-217-206.compute-1.amazonaws.com:9092',
                                                'ec2-54-152-219-229.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             consumer_timeout_ms=10000
                             )
    for message in consumer:
        sum_hum = 0
        room = message.value['room'][0]
        value = message.value['humidity']
        # get each metric value
        for element in value:
            # key is timestamp
            for key in element:
                sum_hum = element[key] + sum_hum
        # get average humidity per sensor
        ave_hum = sum_hum / len(value)
        print(room + ' Average humidity: %.2f' % ave_hum)
        xAxis.append(room)
        yAxis.append(round(ave_hum, 2))
    createGraph("Average Room Humidity", xAxis, yAxis, "%", "hum")


if __name__ == '__main__':
    hum_consumer()

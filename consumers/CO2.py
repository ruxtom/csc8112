from kafka import KafkaConsumer
import json
from graphing import createGraph


def co2_consumer():
    xAxis = []
    yAxis = []
    consumer = KafkaConsumer('usb-co2',
                             bootstrap_servers=['ec2-54-175-3-58.compute-1.amazonaws.com:9092',
                                                'ec2-18-212-22-95.compute-1.amazonaws.com:9092',
                                                'ec2-174-129-110-118.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             consumer_timeout_ms=10000
                             )
    for message in consumer:
        sum_co2 = 0
        room = message.value['room'][0]
        value = message.value['CO2']
        # get each metric value
        for element in value:
            # key is timestamp
            for key in element:
                sum_co2 = element[key] + sum_co2
        # get average CO2 per sensor
        ave_co2 = sum_co2 / len(value)
        print(room + ' Average CO2: %.2f' % ave_co2)
        xAxis.append(str(room))
        yAxis.append(round(ave_co2, 2))
    createGraph("Average Room CO2", xAxis, yAxis, "%", "co2")


if __name__ == '__main__':
    co2_consumer()

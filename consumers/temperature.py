from kafka import KafkaConsumer
from graphing import createGraph
import json


def tem_consumer():
    xAxis = []
    yAxis = []
    consumer = KafkaConsumer('usb-tem',
                             bootstrap_servers=['ec2-54-175-3-58.compute-1.amazonaws.com:9092',
                                                'ec2-18-212-22-95.compute-1.amazonaws.com:9092',
                                                'ec2-174-129-110-118.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             consumer_timeout_ms=10000
                             )
    for message in consumer:
        sum_tem = 0
        room = message.value['room'][0]
        value = message.value['room temperature']
        # get each metric value
        for element in value:
            # key is timestamp
            for key in element:
                sum_tem = element[key] + sum_tem
        # get average temperature per sensor
        ave_tem = sum_tem / len(value)
        print(room + ' Average temperature: %.2f' % ave_tem)
        xAxis.append(room)
        yAxis.append(round(ave_tem, 2))
    createGraph("Average Room Temperature", xAxis, yAxis, "C", "temp")


if __name__ == '__main__':
    tem_consumer()

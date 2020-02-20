from kafka import KafkaConsumer
from graphing import createGraph
import json


def tem_consumer():
    xAxis = []
    yAxis = []
    consumer = KafkaConsumer('usb-tem',
                             bootstrap_servers=['ec2-34-228-191-220.compute-1.amazonaws.com:9092',
                                                'ec2-52-23-217-206.compute-1.amazonaws.com:9092',
                                                'ec2-54-152-219-229.compute-1.amazonaws.com:9092'],
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
        # get average temperature per room
        ave_tem = sum_tem / len(value)
        print(room + ' Average temperature: %.2f' % ave_tem)
        xAxis.append(room)
        yAxis.append(round(ave_tem, 2))
    createGraph("Average Room Temperature", xAxis, yAxis, "temp")


if __name__ == '__main__':
    tem_consumer()

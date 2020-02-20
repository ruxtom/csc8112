import datetime

from kafka import KafkaConsumer
import json


def latency_cosumer():
    time_difference = 0
    sum_value = 0
    consumer = KafkaConsumer('usb-tem',
                             bootstrap_servers=['ec2-34-228-191-220.compute-1.amazonaws.com:9092',
                                                'ec2-52-23-217-206.compute-1.amazonaws.com:9092',
                                                'ec2-54-152-219-229.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                             consumer_timeout_ms=10000
                             )
    for message in consumer:
        sum_value += 1
        time_difference = time_difference + (
                (datetime.datetime.now() - datetime.datetime.strptime(message.value['time'],
                                                                      '%Y-%m-%d %H:%M:%S.%f')).microseconds / 1000)
        ave_time = time_difference / sum_value
        print('Average latency: %.2fms' % ave_time)


if __name__ == '__main__':
    latency_cosumer()

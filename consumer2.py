from kafka import KafkaConsumer
import json


def aws2local2():
    consumer = KafkaConsumer('usb-data', group_id='tem1',
                             bootstrap_servers=['ec2-18-207-191-122.compute-1.amazonaws.com:9092',
                                                'ec2-3-81-136-58.compute-1.amazonaws.com:9092',
                                                'ec2-54-196-123-115.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                             )
    for message in consumer:
        print(message.value)


if __name__ == '__main__':
    aws2local2()

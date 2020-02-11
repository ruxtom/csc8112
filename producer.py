import json
from kafka import KafkaProducer

def send2aws():
    producer = KafkaProducer(
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=['ec2-18-207-191-122.compute-1.amazonaws.com:9092',
                           'ec2-3-81-136-58.compute-1.amazonaws.com:9092',
                           'ec2-54-196-123-115.compute-1.amazonaws.com:9092']
    )
    for i in range(10):
        data = {
            "device": "temperature",
            "tem": 100000,
            "room": i
        }
        print(data)
        producer.send('usb-data', data)
    producer.close()


if __name__ == '__main__':
    send2aws()

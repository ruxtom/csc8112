from kafka import KafkaConsumer
import json


def aws2local():
    consumer = KafkaConsumer('usb-tem',
                             bootstrap_servers=['ec2-34-228-191-220.compute-1.amazonaws.com:9092',
                                                'ec2-52-23-217-206.compute-1.amazonaws.com:9092',
                                                'ec2-54-152-219-229.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                             )
    for message in consumer:
        sum = 0;
        room = message.value['room'][0]
        value = message.value['room temperature']
        for element in value:
            sum = element + sum
        ave = sum / len(value)
        print(room+' Room average temperature: %.2f' % ave)


if __name__ == '__main__':
    aws2local()

from kafka import KafkaConsumer
import json


def dataProcessing():
    consumer = KafkaConsumer('usb-CO2', group_id='CO2_1',
                             bootstrap_servers=['ec2-34-228-191-220.compute-1.amazonaws.com:9092',
                                                'ec2-52-23-217-206.compute-1.amazonaws.com:9092',
                                                'ec2-54-152-219-229.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8'))
                             )
    for message in consumer:
        sum_room = 0
        room = message.value['room'][0]
        value = message.value['CO2']
        for element in value:
            sum_room = element + sum_room
        # get average CO2 per room
        ave = sum_room / len(value)
        print(room + ' Average CO2: %.2f' % ave)


if __name__ == '__main__':
    dataProcessing()

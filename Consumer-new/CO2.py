from kafka import KafkaConsumer
import json


def co2_consumer():
    consumer = KafkaConsumer('usb-co2',
                             bootstrap_servers=['ec2-34-228-191-220.compute-1.amazonaws.com:9092',
                                                'ec2-52-23-217-206.compute-1.amazonaws.com:9092',
                                                'ec2-54-152-219-229.compute-1.amazonaws.com:9092'],
                             value_deserializer=lambda m: json.loads(m.decode('utf-8'))
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
            # get average CO2 per room
        ave_co2 = sum_co2 / len(value)
        print(room + ' Average CO2: %.2f' % ave_co2)


if __name__ == '__main__':
    co2_consumer()

from kafka import KafkaProducer
producer = KafkaProducer(bootsrap_servers='192.168.0.26')
producer.send('sample', b'Hello, World!')
producer.send('sample',key=b'message-two',value=b'This is Kafka-Python')


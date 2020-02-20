# README

The purpose of the project was to allow for ‘smart’ data from the Urban Observatory to be captured, pre-processed on an edge device, streamed continuously and reliably to a cloud service, and then processed further, adding a suitable visualization method for viewing and analyzing the data.
The overall aim was to develop this system so that human interaction was minimal, data processing was automatic, and a number of useful data streams were collected and processed.

## Working Files:

- data_fetcher - runs on the Pi to gather information to send to the AWS Nodes
	- getData.py - process for obtaining the data from the UO-API and extracting the desired sensor values
	- producerThread.py - runs on the Pi to start 3 independant threads for the consumers
- consumers - runs on the AWS Nodes to recieve information and perform data processing
	- CO2.py - collects CO2 data and calculates room averages
	- humidity.py - collects humidity data and calculates room averages
	- temperature.py - collects temperature data and calculates room averages
	- delay.py - collects latency data and calculates average latency
	- graphing.py - used to generate interactive HTML graphs which are stored in the server
- server - runs on the AWS Nodes
	- server.py - starts a simple Flask server to serve static files
	- index.html - basic HTML page whith embedded graphs created by graphing.py

## Technologies used:

- Python 3 and Pycharm
- Urban Observatory API
- Raspberry Pi
- Apache Kafka
- Amazon AWS
- Flask Server

## VNC server running on pi on Matthew's account/email

SSH Running
Local ip: 192.168.0.25 (static wlan0 address)
192.168.0.26 (static eth0 address)

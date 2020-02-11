# README

Project documentation for CSC8112 Coursework, dataflow orchestration.

## Technologies used:

- Python 3 and Pycharm
- Urban Observatory API
- Raspberry Pi
- Apache Kafka
- Amazon AWS

## Documents:

- Data.py - process for obtaining the data from the UO-API and extracting the desired sensor values

## Pi passwd:

IOT2020!d4t4pr0ject

## VNC server running on pi on Matthew's account/email

SSH Running
Local ip: 192.168.0.25 (static wlan0 address)
192.168.0.26 (static eth0 address)

## General

Installed Kafka and Zookeeper on Pi. Following tutorial on [this link](https://aknay.github.io/2017/05/11/how-to-install-zookeeper-and-kafka-in-raspberry-pi-3.html), but have realised this uses an outdated version of Java (JDK 8) and thus the UseParNewGC needs updating, as
this has been deprecated in JDK 9 and 10

### All sensors from sensors/entity with more than one sensor of the same metric. Metric : number of shared sensors
'Room Occupied': 11, 'CO2': 9, 'Chilled Water Valve': 9, 'Low Temperature Hot Water Valve': 9, 'Relative Humidity': 9, 'Room Temperature': 9, 'Cooling Set Point': 6, 'HVAC Operating Mode': 6, 'Heating Set Point': 6, 'BMSTimeSwitch': 3, 'Chilled Water Bypass Valve Status': 3, 'CommsPreCool': 2

### Entity sensors for floor 1 with a shared metric. Metric : number of sensors
'BMSTimeSwitch': 3, 'Chilled Water Bypass Valve Status': 3, 'CommsPreCool': 2

### Entity sensors for floor 2 with a shared metric. Metric : number of sensors
None with more than 1 sensor metric

### Entity sensors for floor 3 with a shared metric. Metric : number of sensors
'Chilled Water Bypass Valve Status': 3, 'BMSTimeSwitch': 2

### Entity sensors for floor 4 with a shared metric. Metric : number of sensors
'BMSTimeSwitch': 3, 'BypassValveStatus': 2

### Entity sensors for floor 5 with a shared metric. Metric : number of sensors
'BMSTimeSwitch': 2, 'BypassValveStatus': 2

### Entity sensors for floor 6 with a shared metric. Metric : number of sensors
'BMSTimeSwitch': 2, 'PlantWest R, DimValStatus': 2, 'CHA LampBallastFailure': 2, 'CHB LampBallastFailure': 2

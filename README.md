# README

Project documentation for CSC8112 Coursework, dataflow orchestration.

## Technologies used:

- Python 3 and Pycharm
- Urban Observatory API
- Raspberry Pi
- Apache Kapfka
- Amaazon AWS

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

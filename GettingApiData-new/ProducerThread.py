import threading
import getData


class sendThread(threading.Thread):
    def __init__(self, threadID, name, metric):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.metric = metric

    def run(self):
        print("Thread Start: " + self.name)
        send_message(self.metric)
        print("Thread End: " + self.name)


def send_message(metric):
    getData.send2cloud(metric)


thread1 = sendThread(1, "temperatureThread", 'room temperature')
thread2 = sendThread(2, "humidityThread", 'humidity')
thread3 = sendThread(3, "CO2Thread", 'CO2')

# Start three independent threads, get temperature, humidity, CO2 from API
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
print("End sending message")

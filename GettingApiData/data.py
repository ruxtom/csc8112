import json, requests



timesToRun = 0
timesToRun = input("How many times to run data collection?")
time = 0

def main():
	global time, timesToRun
	print("in main")
	a = int(timesToRun)
	url = requests.get('https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity')
	print("after url")
	info = json.loads(url.text)
	if time < a:
		time = time + 1
		temperature(info)



def temperature(z):
	if z != None:
		tempSensors = []
		data = []
		for i in z['items']:
			for x in i["feed"]:
				if x["metric"] == "Room Temperature":
					tempSensors.append(x)

	for a in tempSensors:
		for b in a["timeseries"]:
			value = b["latest"]["value"]
			data.append(value)

	print (data)
	main()

#print (info)
main()

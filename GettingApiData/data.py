import json, requests



timesToRun = 0
timesToRun = input("How many times to run data collection?")
time = 0

def main():
	global time, timesToRun
	print("in main")
	a = int(timesToRun)
	url = requests.get('https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity/floor-1')
	print("after url")
	info = json.loads(url.text)
	if time < a:
		time = time + 1
		temperature(info)



def temperature(z):
	if z != None:
		tempSensors = []
		data = []
		#for i in z["items"]:
		for x in z["feed"]:
			if x["metric"] == "C3 HTG Pump Power":
				tempSensors.append(x)

	for a in tempSensors:
		#print(a)
		for b in a["timeseries"]:
			value = b["latest"]["value"]
			data.append(value)

	print (data)
	main()

#print (info)
main()

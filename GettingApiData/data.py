import json, requests

url = requests.get('https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity')

info = json.loads(url.text)
z = info
tempSensors = []
data = []
for i in z["items"]:
	for x in i["feed"]:
		if x["metric"] == "Room Temperature":
			tempSensors.append(x)

for a in tempSensors:
	for b in a["timeseries"]:
		value = b["latest"]["value"]
		data.append(value)

print (data)
#print (info)

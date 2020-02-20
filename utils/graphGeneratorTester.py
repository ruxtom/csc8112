import plotly.graph_objects as go
from time import process_time

# Creates a graph with the given data in the server/public/external_html folder
def createGraph(title, xAxis, yAxis, yAxisTitle, outputFileName):
    tStart = process_time()
    fig = go.Figure(data=go.Bar(x=xAxis, y=yAxis))
    fig.update_layout(title=title, xaxis_title="Room", yaxis_title=yAxisTitle)
    fig.write_html("./server/public/external_html/" + str(outputFileName) +
                   ".html")
    tStop = process_time()
    print("Total graphing time:", tStop-tStart)


if __name__ == '__main__':
    createGraph("Average CO2 %", ["room1", "room2", "room3", "room4"], [12, 5, 3, 2], "%", "co2")
    createGraph("Average Room Temperature", ["room1", "room2", "room3", "room4"], [22, 23, 28, 21], "C", "temp")
    createGraph("Average Humidity %", ["room1", "room2", "room3", "room4"], [23, 5, 10, 12], "%", "hum")
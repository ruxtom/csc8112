import plotly.graph_objects as go
from time import process_time

# Creates a graph with the given data in the server/public/external_html folder
def createGraph(title, xAxis, yAxis, outputFileName):
    tStart = process_time()
    fig = go.Figure(data=go.Bar(x=xAxis, y=yAxis))
    fig.update_layout(title=title)
    fig.write_html("./server/public/external_html/" + str(outputFileName) +
                   ".html")
    tStop = process_time()
    print("Total graphing time:", tStop-tStart)


if __name__ == '__main__':
    createGraph("Average CO2 %", ["room1", "room2", "room3", "room4"], [12, 5, 3, 2], "co2")
import plotly.graph_objects as go
from time import process_time

# Creates a graph with the given data in the server/public/external_html folder
def createGraph(title, xAxis, yAxis, yAxisTitle, outputFileName):
    tStart = process_time()
    fig = go.Figure(data=go.Bar(x=xAxis, y=yAxis))
    fig.update_layout(title=title, xaxis_title="Room", yaxis_title=yAxisTitle)
    fig.write_html("../server/public/external_html/" + str(outputFileName) +
                   ".html")
    # fig.write_html("./server/public/external_html/" + str(outputFileName) +
    #                ".html")
    tStop = process_time()
    print("Total graphing time:", tStop-tStart)

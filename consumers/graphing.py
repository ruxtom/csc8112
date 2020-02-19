import plotly.graph_objects as go


def createGraph(title, xAxis, yAxis, outputFileName):
    fig = go.Figure(data=go.Bar(x=xAxis, y=yAxis))
    fig.write_html("./server/public/external_html/" + str(outputFileName) +
                   ".html")

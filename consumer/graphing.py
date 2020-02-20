import plotly.graph_objects as go


def createGraph(title, data):
    fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
    fig.write_html('first_figure.html', auto_open=True)

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from coinpaprika import client as Coinpaprika

app = Dash(__name__)
server = app.server

client = Coinpaprika.Client()
df = client.historical("btc-bitcoin", start="2021-07-06T00:00:00Z")
#df = px.data.stocks()
#print(df)
fig = px.line(df, x='timestamp', y="price")
app.layout = html.Div([
    html.H4('BTC price line graph'),
    dcc.Graph(id="graph", figure=fig),
])
if __name__ == '__main__':
    app.run_server(debug=True)


# app.run_server(debug=True)
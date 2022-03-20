from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

url = "https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/historical?start=2021-07-06&end=2022-03-01"
res = requests.get(url)
obj=res.json()
df = []
for i in range(len(obj)):
    newdict ={
        "Price" : obj[i]["close"],
        "Date" : obj[i]["time_close"]
    }
    df.append(newdict)
#df = px.data.stocks()
#print(df)
fig = px.line(df, x='Date', y="Price")
app.layout = html.Div([
    html.H4('BTC price line graph'),
    dcc.Graph(id="graph", figure=fig),
])
if __name__ == '__main__':
    app.run_server(debug=True)


# app.run_server(debug=True)


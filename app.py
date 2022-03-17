from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from coinpaprika import client as Coinpaprika

app = Dash(__name__)

client = Coinpaprika.Client()
df = client.historical("btc-bitcoin", start="2021-07-06T00:00:00Z")
#df = px.data.stocks()
#print(df)
fig = px.line(df, x='timestamp', y="price")
app.layout = html.Div([
    html.H4('GOOGLE stock prices'),
    dcc.Graph(id="graph", figure=fig),
])


    


app.run_server(debug=True)
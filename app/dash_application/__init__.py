
import dash
from dash import dcc
from dash import html
from flask import app
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

app = dash.Dash(__name__)

#Fair Market Rent

fmrdata = pd.read_csv('Fair_Market_Rents_1bdr.csv')

fmrfig = px.scatter(fmrdata, x="County", y="Price", color="State", height=2000,
title="1 Bedroom Fair Market Rent Prices By County/State")

fmrfig.update_layout = margin=dict(l=0, r=00, t=00, b=0)

def fair_market_rent(flask_app):
    
    fmr_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname='/fmr/')

    fmr_app.layout = html.Div(children=[

        dcc.Graph(
            id='example-graph',
            figure=fmrfig
        )
    ])

    return fmr_app

@app.callback(
    Output("graph", "figure"), 
    [Input('width', '2000')], 
    [State("graph", "figure")])
def resize_figure(width, fig_json):
    fig = go.Figure(fig_json)
    fig.update_layout(width=int(width))

    return fmrfig


if __name__ == '__main__':
    app.run_server(debug=True)

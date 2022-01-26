
import dash
from dash import dcc
from dash import html
from flask import app
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go

app = dash.Dash(__name__)

#Fair Market Rent 1 Bed 

fmrdata = pd.read_csv('Fair_Market_Rents.csv')

fmrfig = px.scatter(fmrdata, x="County", y="One Bed Price", color="State", height=1000,
title="One Bedroom Properties' Fair Market Rent Prices By County and State")

fmrfig.update_layout = margin=dict(l=0, r=0, t=0, b=0)

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
    fmrfig = go.Figure(fig_json)
    fmrfig.update_layout(width=int(width))

    return fmrfig

#Fair Market Rent 2 Bed 

fmrdata2 = pd.read_csv('Fair_Market_Rents.csv')

fmrfig2 = px.scatter(fmrdata, x="County", y="Two Bed Price", color="State", height=1000,
title="Two Bedroom Properties' Fair Market Rent Prices By County and State")

fmrfig2.update_layout = margin=dict(l=0, r=0, t=0, b=0)

def fair_market_rent2(flask_app):
    
    fmr_app2 = dash.Dash(server=flask_app, url_base_pathname='/fmr2/')

    fmr_app2.layout = html.Div(children=[

        dcc.Graph(
            id='example-graph',
            figure=fmrfig2
        )
    ])

    return fmr_app2

@app.callback(
    Output("graph", "figure"), 
    [Input('width', '2000')], 
    [State("graph", "figure")])
def resize_figure(width, fig_json):
    fmrfig2 = go.Figure(fig_json)
    fmrfig2.update_layout(width=int(width))

    return fmrfig2

#Fair Market Rent 3 Bed 

fmrdata3 = pd.read_csv('Fair_Market_Rents.csv')

fmrfig3 = px.scatter(fmrdata, x="County", y="Three Bed Price", color="State", height=1000,
title="Three Bedroom Properties' Fair Market Rent Prices By County and State")

fmrfig3.update_layout = margin=dict(l=0, r=0, t=0, b=0)

def fair_market_rent3(flask_app):
    
    fmr_app3 = dash.Dash(server=flask_app, url_base_pathname='/fmr3/')

    fmr_app3.layout = html.Div(children=[

        dcc.Graph(
            id='example-graph',
            figure=fmrfig3
        )
    ])

    return fmr_app3

@app.callback(
    Output("graph", "figure"), 
    [Input('width', '2000')], 
    [State("graph", "figure")])
def resize_figure(width, fig_json):
    fmrfig3 = go.Figure(fig_json)
    fmrfig3.update_layout(width=int(width))

    return fmrfig3

#Fair Market Rent 4 Bed 

fmrdata4 = pd.read_csv('Fair_Market_Rents.csv')

fmrfig4 = px.scatter(fmrdata, x="County", y="Four Bed Price", color="State", height=1000,
title="Four Bedroom Properties' Fair Market Rent Prices By County and State")

fmrfig4.update_layout = margin=dict(l=0, r=0, t=0, b=0)

def fair_market_rent4(flask_app):
    
    fmr_app4 = dash.Dash(server=flask_app, url_base_pathname='/fmr4/')

    fmr_app4.layout = html.Div(children=[

        dcc.Graph(
            id='example-graph',
            figure=fmrfig4
        )
    ])

    return fmr_app4

@app.callback(
    Output("graph", "figure"), 
    [Input('width', '2000')], 
    [State("graph", "figure")])
def resize_figure(width, fig_json):
    fmrfig4 = go.Figure(fig_json)
    fmrfig4.update_layout(width=int(width))

    return fmrfig4

if __name__ == '__main__':
    app.run_server(debug=True)

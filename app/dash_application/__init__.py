import dash
from dash import dcc
from dash import html
from flask import app
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

def create_dash_application(flask_app):
    dash_app = dash.Dash(server=flask_app, name="Dashboard", url_base_pathname='/dash/')

    dash_app.layout = html.Div(
        children=[
            html.H1(children='Hello Dash'),
            html.Div(
                children='''
            Dash: A web application framework for your data.
        '''
            ),
            dcc.Graph(
                id='example-graph',
                figure= px.bar(df, x="Fruit", y="Amount", color="City", barmode="group"),  
        )]
    )
    return dash_app


if __name__ == '__main__':
    app.run_server(debug=True)

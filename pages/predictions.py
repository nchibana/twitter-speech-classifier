import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import dash_daq as daq
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import nltk
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS
from textstat.textstat import *
import string
import re
from joblib import load
import numpy as np
# import functions
# from functions import clean
# from functions import tokenize
from functions import wrangle2


from app import app


model = load('assets/model.joblib')
# vectorizer = load('assets/vectorizer.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown('## Enter tweet text below:', className='mb-5', style={'marginTop': '1em'}), 
        dcc.Textarea(
            id='input-box',
            placeholder='Maximum length of 280 characters...',
            value='Rosie is crude, rude, obnoxious and dumb - other than that I like her very much!',
            cols=50,
            rows=6,
            maxLength=280,
            style={'width': '100%', 'marginBottom': '1.2em'}
    ),
        html.Button('Offensive or not?', id='button', n_clicks=1, style={
            'width':'10em', 'padding': '5px', 'marginBottom': '4em'}),
        dcc.Markdown('### Predicted Probabilities:', style={'marginBottom': '2em'}), 
        html.Div(id='prediction-label', className='lead', style={'marginBottom': '3em', 'fontWeight': 'bold', 'fontSize': '20px'}), 
        html.Div(id='prediction-table', style={'marginBottom': '5em'}),
    ],
    md=5,
)

column2 = dbc.Col(
    [
        html.Div(id='prediction-gauge', style={'marginTop': '6.2em'})
        # html.Div(id='prediction-label', className='lead'),
        # html.Div(id='prediction-table', className='lead')
    ]
)

layout = dbc.Row([column1, column2])

@app.callback(
    [Output('prediction-label', 'children'),Output('prediction-table', 'children'), Output('prediction-gauge', 'children')],
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')]
)
def predict(clicked, text):
    if clicked:
        text = [text]
        text = wrangle2(text)
        y_pred = model.predict(text)
        if y_pred == 0:
            y_pred = 'hateful'
        if y_pred == 1:
            y_pred = 'offensive'
        if y_pred == 2:
            y_pred = 'normal'
        df = pd.DataFrame(model.predict_proba(text), columns=["Hateful", "Offensive", "Normal"])
        df_percent = df.mul(100).round(2).astype(str) + '%'
        output1 = f'This tweet is labeled as {y_pred}.'
        output2 =  dash_table.DataTable(
            data=df_percent.to_dict('records'),
            style_cell={'textAlign': 'left', 'padding': '15px'},
            columns=[{"name": i, "id": i} for i in df_percent.columns],
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontSize': '15px',
                'fontWeight': 'bold'
    }
        )
        output3 = daq.Gauge(
            showCurrentValue=True,
            units="percentage points",
            value=(((df[["Hateful", "Offensive", "Normal"]].max()).max())*100).round(2),
            label=f'Percent probability this tweet is {y_pred}',
            size=380,
            labelPosition='bottom',
            max=100,
            min=0,
)  

        return output1, output2, output3
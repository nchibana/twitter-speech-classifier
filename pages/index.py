import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smallersize screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Detect Hate Speech Online

            ********

            Online platforms are tackling the problem of hate speech every day, but it can be difficult to draw the line between what is protected under free speech laws and what infringes on others' rights.

            * The Twitter Hate Speech detector is an app that aims to help identify hateful and offensive online speech.

            * The model used to make these predictions was trained on a combination of two labeled datasets, with a total of 102,840 tweets.
            
            * 56 percent of them were labeled "Normal", 39 percent as "Offensive" and 5 percent as "Hateful".

            """
        ),
        dcc.Link(dbc.Button('Score Your Tweet', color='primary', style=dict(marginTop=40, marginBottom=200)), href='/predictions')
    ],
    md=4,
)

colors = ['lightslategray',] * 10
colors[0] = 'crimson'

x = ['hate', 'like','n**ga','f**king','n**gas', 'b*tch', 'as*', 'people','get', 'amp']
y = [679, 591, 571, 552, 483, 439, 362, 346, 340, 328]

fig = go.Figure(data=[go.Bar(
    x=x,
    y=y,
    marker_color=colors # marker color can be a single color value or an iterable
)])
fig.update_layout(title_text='Most Common Words in Tweets Labeled Hateful')


column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.figure_factory as ff

from app import app



column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights  

            ********

            Emphasize how the app will benefit users. Don't emphasize the underlying technology.

            * RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

            * RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

            * RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

            * RUN is a running app that adapts to your fitness levels and designs.


            """
        ),
         html.Iframe(src='https://twitframe.com/show?url=https%3A%2F%2Ftwitter.com%2FrealDonaldTrump%2Fstatus%2F1154112475002036234', style=dict(border=0, padding=40), height=300, width=550),
         html.Iframe(src='https://twitframe.com/show?url=https%3A%2F%2Ftwitter.com%2FNatashaBertrand%2Fstatus%2F1157063129555177473', style=dict(border=0, padding=40), height=300, width=550),
         dcc.Markdown(
            """
            Emphasize how the app will benefit users. Don't emphasize the underlying technology.

            RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

            RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

            RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

            RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.
            

            """
        ),


    ],
    md=6,
)

##Figure 1

z=[[1463, 1462, 1545],
    [1962, 26903, 3269],
    [1038, 2082, 43116]]

colorscale=[[0, 'navy'], [1, 'plum']]
font_colors = ['white', 'black']
y=['A-0','A-1', 'A-2']
x=['P-0','P-1', 'P-2']
x_labels=['Predicted Hate','Predicted Offensive', 'Predicted Normal']
y_labels=['Actual Hate','Actual Offensive', 'Actual Normal']
hovertext = list()
for yi, yy in enumerate(y_labels):
    hovertext.append(list())
    for xi, xx in enumerate(x_labels):
        hovertext[-1].append('{}<br />{}<br />{}'.format(xx, yy, z[yi][xi]))

fig1 = ff.create_annotated_heatmap(z, x=x, y=y, xgap = 3, ygap = 3, hoverinfo="text", text=hovertext, annotation_text=z, colorscale=colorscale, font_colors=font_colors)

fig1.update_layout(
    title='Confusion Matrix for Twitter Hate Speech Type Classifier',
    # margin=dict(
    #     pad=10
    # ),
    xaxis = dict(
    # showticklabels=False,
    ticks = ""
  ),
    yaxis = dict(
    # showticklabels=False,
    ticks = "",
  )
)


##Figure 2




column2 = dbc.Col(
    [
        dcc.Graph(figure=fig1),
        dcc.Markdown(
            """
            Emphasize how the app will benefit users. Don't emphasize the underlying technology.

            RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

            RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

            RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

            RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

            RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.

            RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.

            """
        ),
       
        
    ],
    md=6,
)

layout = dbc.Row([column1, column2])
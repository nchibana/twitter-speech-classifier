import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.metrics import roc_curve
import pandas as pd
from joblib import load

from app import app



#Figure 3

# data = load('notebooks/fprtpr.joblib')

x = load('notebooks/fpr2.joblib')
y = load('notebooks/tpr2.joblib')

# fig3 = px.line(data, x='fpr', y='tpr', title='Life expectancy in Canada')

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=x, y=y, name="linear",
                    line_shape='linear'))

fig3.update_layout(title='ROC Curve for Binary Twitter Speech Classifier',
                   xaxis_title='False Positive Rate',
                   yaxis_title='True Positive Rate')


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights  

            ********

            After several iterations of training and testing, the model yields somewhat accurate results for tweets that are similar to those in the original dataset.

            * The multiclass classifier has an accuracy score of 86%, a precision score of 90% for normal speech, but only 33% precision and recall for hateful speech detection.

            * This is probably due to the existence of class imbalance, as only 5% of the tweets in the dataset were labeled hateful. To address this issue, the class weight
            for the logistic regression model used was set to "balanced."

            * As a binary classifier that distinguishes between hateful/offensive tweets and normal ones, the accuracy of the model increases to 90%, with 91% precision and 87% recall.


            """
        ),
         html.Iframe(src='https://twitframe.com/show?url=https%3A%2F%2Ftwitter.com%2FrealDonaldTrump%2Fstatus%2F1154112475002036234', style=dict(border=0, padding=40, marginTop=40), height=300, width=550),
         html.Iframe(src='https://twitframe.com/show?url=https%3A%2F%2Ftwitter.com%2FNatashaBertrand%2Fstatus%2F1157063129555177473', style=dict(border=0, padding=40), height=300, width=550),
         dcc.Markdown(
            """
            The classification report for the binary hate speech classifier reveals that the scores are drastically better when both hateful and offensive tweets are combined into one label.

            The reason for this might be that the difference between hateful and offensive tweets is not sufficiently well defined. 
            
            Given that human labelers all have different subjective criteria by which they differentiate between hateful and offensive speech, it would be worth investigating this difference further.
            
            Also, as mentioned above, the class imbalance contributes greatly to the low precision and recall scores for the multiclass model. 
            
            For future studies, the minority class may be oversampled to determine whether this improves the performance of the model.



            """
        ),
        dcc.Graph(figure=fig3, style={'marginTop': '2.5em'}),


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
    title='Confusion Matrix for Multiclass Twitter Speech Classifier',
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

df = pd.read_csv('https://raw.githubusercontent.com/nchibana/twitter-speech-classifier/master/notebooks/data/report.csv', index_col=0)

fig2 = go.Figure(data=[go.Table(
    columnwidth = [400,300,300,300],
    header=dict(values=[''] + list(df.columns),
                align='left'),
    cells=dict(values=[['False', 'True', 'micro avg', 'macro avg', 'weighted avg'], df['Precision'], df['Recall'], df['f1-Score']],
               align='left',
               height=60))
])

fig2.update_layout(title='Classification Report for Binary Twitter Speech Classifier')




column2 = dbc.Col(
    [
        dcc.Graph(figure=fig1, style={'marginTop': '2.5em'}),
        dcc.Markdown(
            """
            As an example of a misclassified tweet, this post by Donald Trump was labeled as "offensive" by the model, even though it would not be classified as such by human labelers.

            According to the studies for which this data was collected, “any speech that attacks a person or group on the basis of race, religion, ethnic origin, 
            national origin, gender, disability, sexual orientation, or gender identity” is defined as hateful. 
            
            Meanwhile, offensive language is defined as any profane, derogatory or abusive language. The latter is probably the reason why the second tweet to the left was also misclassified by the model as an "offensive" tweet. 
            
            Certain terms that are used in a vulgar or offensive manner might have different meanings in a completely different context, as in this case.

            After analyzing the coefficients for the logistic regression model used, it was found that the features with most importance were sentiment scores calculated by the VADER
            analysis tool.
            
            Also important were the number of mentions in the tweet and number of terms in the tweet, which explains why some shorter tweets are often misclassified as offensive or hateful.

            """
        ),

        dcc.Graph(figure=fig2, style={'marginTop': '3em'}),

         dcc.Markdown(
            """
            
            The large area under the ROC curve for the binary version of this classifier reveals that it can distinguish accurately between hateful/offensive tweets and normal ones.

            Speaking in terms of practical applications of this model, however, it would be beneficial to differentiate between a greater variety of speech types than just hateful/offensive
            and neutral ones.

            For example, there may be tweets that contain profane or vulgar language but stop short of hate speech. These could still potentially be protected by free speech laws. Hate speech, on the
            other hand, is speech directed at a specific person of group of people that may incite violence.

            While there is room for debate on all these questions, in the meantime, Twitter has taken the safe route by deleting accounts that contain any mention of violence, swear words
            or trigger phrases that promote violence or self-harm, even if they were not authored by the owner of the account.
            

            """
        ),

        
       
        
    ],
    md=6,
)

layout = dbc.Row([column1, column2])
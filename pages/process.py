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




column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process 

            ********

            To build this model, two datasets with similar labels were combined to form a dataset with 102,840 observations. 
            
            I would like to thank the research team behind [this study](https://arxiv.org/pdf/1802.00393.pdf), as they promptly gave me access to their data, which was labeled through Crowdflower. 
            
            This model builds largely on their work, as well as that of [this previous study](https://aaai.org/ocs/index.php/ICWSM/ICWSM17/paper/view/15665).

            After gaining access to both datasets, I proceeded to retrieve the corresponding tweet text for all IDs in the second set (as it was not provided) via Twitter's API. 
            
            This was [the code](https://stackoverflow.com/questions/44581647/retrieving-a-list-of-tweets-using-tweet-id-in-tweepy) I used to retrieve the text, without exceeding the rate limit.

            """
        ),
         html.Iframe(src='data:text/html;charset=utf-8,%3Cbody%3E%3Cscript%20src%3D%22https%3A%2F%2Fgist.github.com%2Fnchibana%2F20d6d9f8ae62a6cc36b773d37dd7dc70.js%22%3E%3C%2Fscript%3E%3C%2Fbody%3E', style=dict(border=0, padding=40), height=780, width=1000),
         dcc.Markdown(
            """
            
            After that, I proceeded to combine the datasets and eliminate all duplicate tweets. I also defined a baseline accuracy score of 56%, which is the percent accuracy the model would achieve
            if it predicted the majority class for all tweets.

            Using some of the processes followed by the studies mentioned above, I also continued to preprocess the data by eliminating excess spaces, removing punctuation and retrieving the stem words of terms
            used in tweets.

            Next, I used Scikit-learn's [TfidVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to convert tweet text into a matrix of
            TF-IDF features, which is a statistic that calculates how important a word is to a document or collection of words.
            

            """
        ),

       html.Iframe(src='data:text/html;charset=utf-8,%3Cbody%3E%3Cscript%20src%3D%22https://gist.github.com/nchibana/c15cbc4a1d97af02fa62fff5868bc36e.js%22%3E%3C%2Fscript%3E%3C%2Fbody%3E', style=dict(border=0, padding=40), height=460, width=1000),

            dcc.Markdown(
            """
            
            To increase the accuracy of the model, additional features were engineered, such as the number of syllables per word, the total number of characters, the number of words, the number of unique
            terms, as well as readability and sentiment scores for each tweet.

            Additionally, the number of mentions, hashtags and links in each tweet were also counted. For this study, images or any other type of media content were not analyzed. 

            """
         ),

      html.Iframe(src='data:text/html;charset=utf-8,%3Cbody%3E%3Cscript%20src%3D%22https%3A%2F%2Fgist.github.com%2Fnchibana%2F5cebfbfa700974edcd9f5fa6e43cc513.js%22%3E%3C%2Fscript%3E%3C%2Fbody%3E', style=dict(border=0, padding=40), height=600, width=1000),

        dcc.Markdown(
            """
            
            After testing several models such as Linear SVC, I finally settled on a logistic regression model which I trained on the data and used for the final model and app.

            I also used grid search to find the optimal parameters for this logistic regression model.

            Finally, I computed all accuracy scores and proceeded to plot visualizations to help me get a deeper understanding of the model, such as a confusion matrix to visualize misclassified tweets.

            """
         ),
    html.Iframe(src='data:text/html;charset=utf-8,%3Cbody%3E%3Cscript%20src%3D%22https%3A%2F%2Fgist.github.com%2Fnchibana%2F0cc0c44c9b5a991adbc2690c97023d0c.js%22%3E%3C%2Fscript%3E%3C%2Fbody%3E', style=dict(border=0, padding=40), height=300, width=1000),
        dcc.Markdown(
            """
            ## Sources

            ********

            1. Automated Hate Speech Detection and the Problem of Offensive Language
            Davidson, Thomas and Warmsley, Dana and Macy, Michael and Weber, Ingmar
            Proceedings of the 11th International AAAI Conference on Web and Social Media p. 512-515. 2017 

            2. Large Scale Crowdsourcing and Characterization of Twitter Abusive Behavior
            Founta, Antigoni-Maria and Djouvas, Constantinos and Chatzakou, Despoina and Leontiadis, Ilias and Blackburn, Jeremy and Stringhini, Gianluca and Vakali, Athena and Sirivianos, Michael and Kourtellis, Nicolas
            11th International Conference on Web and Social Media, ICWSM 2018 2018 

            """
         ),

    ],
    md=12,
)



layout = dbc.Row([column1])
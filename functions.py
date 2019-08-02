import pandas as pd
import nltk
import numpy as np
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS
from textstat.textstat import *
from joblib import load
import string
import re


def clean(text):
    spaces = '\s+'
    urls = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
                '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    mentions = '@[\w\-]+'
    parsed_text = re.sub(spaces, ' ', text)
    parsed_text = re.sub(urls, '', parsed_text)
    parsed_text = re.sub(mentions, '', parsed_text)
    return parsed_text


def tokenize(text):
    stemmer = PorterStemmer()
    text = " ".join(re.split("[^a-zA-Z]*", text.lower())).strip()
    tokens = [stemmer.stem(t) for t in text.split()]
    return tokens

def wrangle2(text):
    stopwords=pd.read_table("english").values.tolist()
    stopwords=sum(stopwords , [])
    other_exclusions = ["#ff", "ff", "rt"]
    stopwords.extend(other_exclusions)

    stemmer = PorterStemmer()


    def clean(text):
        spaces = '\s+'
        urls = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
            '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        mentions = '@[\w\-]+'
        parsed_text = re.sub(spaces, ' ', text)
        parsed_text = re.sub(urls, '', parsed_text)
        parsed_text = re.sub(mentions, '', parsed_text)
        return parsed_text
    
    def tokenize(text):
        text = " ".join(re.split("[^a-zA-Z]*", text.lower())).strip()
        tokens = [stemmer.stem(t) for t in text.split()]
        return tokens

    vectorizer = load('assets/vectorizer_final.joblib')


    # vectorizer = TfidfVectorizer(
    #     tokenizer=tokenize,
    #     preprocessor=clean,
    #     ngram_range=(1, 3),
    #     stop_words=stopwords,
    #     use_idf=True,
    #     smooth_idf=False,
    #     norm=None,
    #     decode_error='replace',
    #     max_features=10000,
    #     min_df=5,
    #     max_df=0.501
    #     )
    
    tfidf = vectorizer.transform(text).toarray()
    vocab = {v:i for i, v in enumerate(vectorizer.get_feature_names())}
    idf_vals = vectorizer.idf_
    idf_dict = {i:idf_vals[i] for i in vocab.values()}
    
    sentiment_analyzer = VS()

    def count_twitter_objs(text):
    
        space_pattern = '\s+'
        giant_url_regex = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
            '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        mention_regex = '@[\w\-]+'
        hashtag_regex = '#[\w\-]+'
        parsed_text = re.sub(space_pattern, ' ', text)
        parsed_text = re.sub(giant_url_regex, 'URLHERE', parsed_text)
        parsed_text = re.sub(mention_regex, 'MENTIONHERE', parsed_text)
        parsed_text = re.sub(hashtag_regex, 'HASHTAGHERE', parsed_text)
        return(parsed_text.count('URLHERE'),parsed_text.count('MENTIONHERE'),parsed_text.count('HASHTAGHERE'))

    def other_features(text):
        sentiment = sentiment_analyzer.polarity_scores(text)

        words = clean(text) #Get text only

        syllables = textstat.syllable_count(words) #count syllables in words
        num_chars = sum(len(w) for w in words) #num chars in words
        num_chars_total = len(text)
        num_terms = len(text.split())
        num_words = len(words.split())
        avg_syl = round(float((syllables+0.001))/float(num_words+0.001),4)
        num_unique_terms = len(set(words.split()))

        FKRA = round(float(0.39 * float(num_words)/1.0) + float(11.8 * avg_syl) - 15.59,1)

        FRE = round(206.835 - 1.015*(float(num_words)/1.0) - (84.6*float(avg_syl)),2)

        twitter_objs = count_twitter_objs(text) #Count #, @, and http://
        retweet = 0
        if "rt" in words:
            retweet = 1
        features = [FKRA, FRE,syllables, avg_syl, num_chars, num_chars_total, num_terms, num_words,
                    num_unique_terms, sentiment['neg'], sentiment['pos'], sentiment['neu'], sentiment['compound'],
                    twitter_objs[2], twitter_objs[1],
                    twitter_objs[0], retweet]

        return features

    def get_feature_array(text):
        feats=[]
        for t in text:
            feats.append(other_features(t))
        return np.array(feats)
    
    feats = get_feature_array(text)
    
    all = np.concatenate([tfidf,feats],axis=1)
    
    other_features_names = ["FKRA", "FRE","num_syllables", "avg_syl_per_word", "num_chars", "num_chars_total", \
                        "num_terms", "num_words", "num_unique_words", "vader neg","vader pos","vader neu", "vader compound", \
                        "num_hashtags", "num_mentions", "num_urls", "is_retweet"]

    variables = ['']*len(vocab)
    for k,v in vocab.items():
        variables[v] = k

    features = variables+other_features_names
    X = pd.DataFrame(all)
    
    
    return X






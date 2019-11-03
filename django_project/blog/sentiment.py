#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import time
import re
import nltk
from sklearn.externals import joblib
import pandas as pd
import tweepy
from textblob import TextBlob

def sentiment_func(sent):
    analysis=TextBlob(sent)
    return analysis.sentiment.polarity

def polarity_func(score):
    if score==0.0:
        return 'neutral'
    if score>0.0:
        return 'positive'
    if score<0.0:
        return 'negative'

def sentiment2target(sentiment):
    return {
        'negative': -1,
        'neutral': 0,
        'positive' : 1
    }[sentiment]




# In[2]:


def preprocessTweets(tweet):
    
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    
    #Convert @username to __HANDLE
    tweet = re.sub('@[^\s]+','__HANDLE',tweet)  
    
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    
    #trim
    tweet = tweet.strip('\'"')
    
    # Repeating words like happyyyyyyyy
    rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE)
    tweet = rpt_regex.sub(r"\1\1", tweet)
    
    #Emoticons
    emoticons =     [
     ('__positive__',[ ':-)', ':)', '(:', '(-:', \
                       ':-D', ':D', 'X-D', 'XD', 'xD', \
                       '<3', ':\*', ';-)', ';)', ';-D', ';D', '(;', '(-;', ] ),\
     ('__negative__', [':-(', ':(', '(:', '(-:', ':,(',\
                       ':\'(', ':"(', ':((', ] ),\
    ]

    def replace_parenth(arr):
       return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]
    
    def regex_join(arr):
        return '(' + '|'.join( arr ) + ')'

    emoticons_regex = [ (repl, re.compile(regex_join(replace_parenth(regx))) )             for (repl, regx) in emoticons ]
    
    for (repl, regx) in emoticons_regex :
        tweet = re.sub(regx, ' '+repl+' ', tweet)

     #Convert to lower case
    tweet = tweet.lower()
    
    return tweet


# In[3]:


def stem(tweet):
        stemmer = nltk.stem.PorterStemmer()
        tweet_stem = ''
        words = [word if(word[0:2]=='__') else word.lower()                     for word in tweet.split()                     if len(word) >= 3]
        words = [stemmer.stem(w) for w in words] 
        tweet_stem = ' '.join(words)
        return tweet_stem


# In[4]:


def predict(tweet,classifier):
    
    tweet_processed = stem(preprocessTweets(tweet))
             
    if ( ('__positive__') in (tweet_processed)):
         sentiment  = 1
         return sentiment
        
    elif ( ('__negative__') in (tweet_processed)):
         sentiment  = 0
         return sentiment       
    else:
        
        X =  [tweet_processed]
        sentiment = classifier.predict(X)
        return (sentiment[0])


# In[8]:
def processTweets(X_test):
        X_test = [stem(preprocessTweets(tweet)) for tweet in X_test]
        return X_test

def main():
    print('Loading the Classifier, please wait....')
    classifier = joblib.load('svmClassifier.pkl')
    print('READY')
    tweet = ' '
    for tweet in sys.stdin:
            print(predict(tweet, classifier))
            
            
            


# In[ ]:





# In[ ]:





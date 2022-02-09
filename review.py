import pandas as pd
import spacy
import numpy as np
import json
import nltk
from nltk import FreqDist
import re
import gzip
import gensim
from gensim import corpora
import pyLDAvis
import matplotlib.pyplot as plt
import seaborn as sns


nlp = spacy.load("en_core_web_sm")
fileName = 'West Elm Consumer Affair.csv'
df = pd.read_csv(fileName, header=0)
df = df[df['Rating'].isin([3, 4, 5]) == False]
# df = df.drop(columns=['Field1', 'Field2', 'Field3', 'Root'])
# df.to_csv(fileName, index=False)

#visualize common words
def freq_words(x, terms = 15):
  all_words = ' '.join([text for text in x])
  all_words = all_words.split()
  
  fdist = FreqDist(all_words)
  words_df = pd.DataFrame({'word':list(fdist.keys()), 'count':list(fdist.values())})
  
  # selecting top 20 most frequent words
  d = words_df.nlargest(columns="count", n = terms) 
  plt.figure(figsize=(20,5))
  ax = sns.barplot(data=d, x= "word", y = "count")
  ax.set(ylabel = 'Count')
  plt.show()

#convert star to number rating
def getRating():
     for index, rating in enumerate(df["Rating"]):
        rate = int(rating[0])
        df.loc[index, 'Rating'] = rate
        df.to_csv(fileName, index=False)
 
comments = []
cleanedComments = []
def cleanComment():
    
    for comment in comments:
        doc = nlp(comment)

        #remove stop words
        filtered_tokens = [token for token in doc if not token.is_stop]
        #normalize
        for token in filtered_tokens:          
            cleanedComments.append(token.lemma_)

def getComment():
    df['Content'].replace('', np.nan, inplace = True)
    df.dropna(subset=['Content'], inplace = True)
    # df['Rating'].replace('', np.nan, inplace = True)
    # df.dropna(subset=['Rating'], inplace = True)
    df['Content'] = df['Content'].str.replace("n\'t", " not")
    df['Content'] = df['Content'].str.replace("[^a-zA-Z]+", " ")
    df['Content'] = df['Content'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>2]))
    
    for comment in df["Content"]:
        #if (df.loc[comment, 'Rating'] == 1 or df.loc[comment, 'Rating'] == 2):
        comments.append(comment)
           
        if len(comments) >= 700:
            cleanComment()
            freq_words(cleanedComments)
            break 


getComment()
#getRating()       



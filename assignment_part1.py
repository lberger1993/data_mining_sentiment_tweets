import pandas as pd
from data.filters.filter import filter_words

if __name__ == '__main__':
    all_tweets = pd.DataFrame.from_csv('data/trainingTweets.csv', index_col=None)
    #all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
    filter_words(all_tweets)

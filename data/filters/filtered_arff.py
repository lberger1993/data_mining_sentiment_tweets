import pandas as pd
from generate_arff import count_words, print_arff, remove_stop_words

negative_word_list = list()
positive_word_list = list()


def get_negative_words():
    for line in open('/Users/luciaeve/Documents/EMSE/code/data_mining_sentiment_tweets/data/filters/data/negative.txt'):
        line = line.replace('\n', "")
        negative_word_list.append(line)
    return negative_word_list


def get_positive_words():
    for line in open('/Users/luciaeve/Documents/EMSE/code/data_mining_sentiment_tweets/data/filters/data/positive.txt'):
        line = line.replace('\n', "")
        positive_word_list.append(line)
    return positive_word_list


def filter_words(data_frame):
    total_list = get_positive_words() + get_negative_words()
    data_frame['tweet'] = data_frame['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
    data_frame['tweet'] = data_frame['tweet'].apply(lambda x: [item for item in x if item in total_list])
    return data_frame


all_tweets = pd.DataFrame.from_csv('data/tweets.csv', index_col=None)
temp_csv = filter_words(all_tweets)
temp_csv.to_csv('data/pos_neg.csv')
all_tweets = pd.DataFrame.from_csv('data/pos_neg.csv', index_col=None)
all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
all_tweets = remove_stop_words(all_tweets)
topWords = count_words(all_tweets).most_common(int(500))
print_arff(all_tweets, topWords, 'filtered', 500)


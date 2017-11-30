import pandas as pd
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
    print(data_frame['tweet'])
    return data_frame

# testing
df = pd.DataFrame.from_csv('data/test.csv', index_col=None)
filter_words(df)


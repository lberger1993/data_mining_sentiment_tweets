import pandas as pd
import json
import collections
import itertools
from stopwords import get_stop_words

def remove_stop_words(df):
    df['tweet'] = df['tweet'].apply(lambda x: [item for item in x if item not in get_stop_words()])
    return df

def count_words(df):
    totals = collections.Counter(i for i in list(itertools.chain.from_iterable(df['tweet'])))
    print(totals)
    # with open('data/system_generated/most_common_words.json', 'w') as outfile:
    #     json.dump(dict(totals.most_common()), outfile)
    return totals


def select_top_words():
    with open('data/system_generated/most_common_words.json', 'r') as wordsfile:
        data = json.load(wordsfile)
        data = {word: count for word, count in data.items() if data[word] > 5}
        data = data[:50]
        print(data)
        return data


def print_arff(tweets, attributes, attr_count, file_name):
    with open("data/system_generated/"+ str(file_name) + str(attr_count) + ".arff", "w") as file:
        file.write("%\n")
        file.write("% Tweet Attributes\n")
        file.write("%\n")
        file.write("@relation 'tweeterfeed'\n")
        file.write("@attribute tweetID numeric\n")
        for item in attributes:
            file.write("@attribute '%s' {'n', 'y'}\n" % item[0])
        file.write("@attribute 's_label' {'0','1','2','4'}")
        file.write("\n@data\n")
        for index, row in tweets.iterrows():
            line = "%d" % row['other']
            for item in attributes:
                if item[0] in row['tweet']:
                    line += ", 'y'"
                else:
                    line += ", 'n'"
            line += ", %s" % str(row['id'])
            line += "\n"
            file.write(line)
            # print(row['other'],row['tweet'])

# testing
all_tweets = pd.DataFrame.from_csv('data/tweets.csv', index_col=None)
all_tweets['tweet'] = all_tweets['tweet'].str.lower().str.replace('[^\w\s]', '').str.split()
all_tweets = remove_stop_words(all_tweets)
topWords = count_words(all_tweets).most_common(int(500))
print_arff(all_tweets, topWords, 'unfiltered', 500)
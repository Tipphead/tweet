import pandas
import re

df = pandas.read_csv(r'X:\Twitter_Project\Datasets\Trumps Legcy\Trumps Legcyfixed.txt')  # Dataframe with all data
text = pandas.Series(df.text)  # tweet text
hashtags_list = []
for t in text:
    hashtags_list = (re.findall(r'#\w+', t))  # hashtags in order of dataframe
hashtags_drop = []
for h in hashtags_list:  # hashtags without empty lists inside
    if h:
        hashtags_drop.append(h)
hashtags_drop = pandas.Series(hashtags_drop, dtype='string')  # list to series for viewing
hashtags_individual = []
for h in hashtags_drop:  # if more than one hashtag per tweet, put into new index
    for a in h:
        hashtags_individual.append(a)

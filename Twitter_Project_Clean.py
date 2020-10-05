#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:54:36 2020

@author: j
"""

import numpy as np
import pandas
import re
import wordsegment as ws
from Twitter_Project.py import search

#read
data = pandas.read_csv("./TrumpTweets08262020toBeginning")
#tweet text of all rows
tweet_text = data['text']
#tweets that have hash tags (use iloc)
tweet_text_with_tags = tweet_text[tweet_text[:].astype(str).str.contains('#')]
#search method for finding words beginning with '#'
n = len(tweet_text_with_tags)
hash_tags_with_duplicates = []
search(n)
#df for all hashtags ever tweeted
hash_tags_df = pandas.DataFrame(hash_tags_with_duplicates[:])
first_column = hash_tags_df.loc[:,0]
second_column = hash_tags_df.loc[:,1]
#n = column number
#nth_column = hash_tags_df.loc[:,n:n]

#put all columns into one column
for i in range(1, len(hash_tags_df.columns)):
    final_column_df = first_column.append(hash_tags_df.loc[:,i],ignore_index=True)
#remove duplicates and put into dataframe    
hash_tags_no_duplicate_df = pandas.DataFrame(final_column_df.drop_duplicates())
#all hash tags to txt
final_column_df.to_csv("hash_tags_duplicates_df.txt")
#singular hash tags to txt
hash_tags_no_duplicate_df.to_csv("hash_tags_no_duplicate_df.txt",index=False,header=False)
#create dictionary for hashtags and frequency
counts = dict()
for hashtag in final_column_df:
    if hashtag in counts:
        counts[hashtag] += 1
    else:
        counts[hashtag] = 1
#write frequency file
with open('counts_dict.txt', 'w') as f:
    print(counts, file=f)
#edit frequency file
with open('counts_dict.txt', "r") as file:
    filedata = file.read()
# Replace the target string
filedata = filedata.replace(',', "\n")
filedata = filedata.replace('{', "")
filedata = filedata.replace('}', "")
filedata = filedata.replace("'", "")
filedata = filedata.replace(' ', "")
# Write the file out again
with open('counts_dict.txt', "w") as file:
    file.write(filedata)
#write singluar hashtags and frequencies to file
hash_tag_frequency_df = pandas.read_csv('counts_dict.txt')
hash_tag_frequency_df.to_html('hash_tag_frequency_df.html')
#separate hashtag words
ws.load()
with open('hash_tags_no_duplicate_df.txt', "r") as file:
     line = file.readline()
     with open('hash_tags_no_duplicate_df_sep.txt', 'w') as newfile:
         while line:
             print(ws.segment(line), file=newfile)
             line = file.readline()


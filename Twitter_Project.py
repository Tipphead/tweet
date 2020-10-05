#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:09:02 2020

@author: j
"""

import numpy as np
import pandas
import re
import wordsegment as ws

#read
data = pandas.read_csv("./TrumpTweets08262020toBeginning")
#data = pandas.read_csv("./TrumpTweetsTestData100")
#indexed list of columns
col_mapping = [f"{c[0]}:{c[1]}" for c in enumerate(data.columns)]
#dictionary collection of columns
col_mapping_dict = {c[0]:c[1] for c in enumerate(data.columns)}
#tweet text of all rows
tweet_text = data['text']
#tweets with '#' removed
tweet_text_no_tags = tweet_text[:].str.split('#')
#tweets that have hash tags (use iloc)
tweet_text_with_tags = tweet_text[tweet_text[:].astype(str).str.contains('#')]
#dataframe with added column "text_tags" -- gives location in string of hashtag
data["text_tag_locations"]= data["text"].str.find('#')
#index of where hashtag is located in list of tweets with hashtags
hash_tag_index = tweet_text_with_tags[:].str.find('#')


#search method for finding words beginning with '#'
n = len(tweet_text_with_tags)
hash_tags_with_duplicates = []
def search(n):
    t = lambda x: re.findall(r'(?<=#)\w+', tweet_text_with_tags.iloc[x])
    for x in range(n):
        hash_tags_with_duplicates.append(t(x)) 
    return hash_tags_with_duplicates

search(n)

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


counts = dict()
for hashtag in final_column_df:
    if hashtag in counts:
        counts[hashtag] += 1
    else:
        counts[hashtag] = 1

with open('counts_dict.txt', 'w') as f:
    print(counts, file=f)
    
    

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
    
    

hash_tag_frequency_df = pandas.read_csv('counts_dict.txt')
hash_tag_frequency_df.to_html('hash_tag_frequency_df.html')
    




ws.load()

with open('hash_tags_no_duplicate_df.txt', "r") as file:
     line = file.readline()
     with open('hash_tags_no_duplicate_df_sep.txt', 'w') as newfile:
         while line:
             print(ws.segment(line), file=newfile)
             line = file.readline()

# print(ws.segment("ThiSISATeSt")) #segment will clean the text
# output = ['this', 'is, 'a', 'test']
# print(ws.clean("ThiSISATest")) #or you can clean it yourself
# output = thisisatest


#   with open('hash_tags_no_duplicate_df.txt', 'r') as reader:
#       lines = (line.split('\t') for line in reader)
#       dict((word, float(number)) for word, number in lines)

# with open('hash_tags_duplicates_df.txt') as reader:
#     lines = reader.read().split('\n')

# load the input text file
# text = open('hash_tags_duplicates_df.txt', 'r').readlines()




























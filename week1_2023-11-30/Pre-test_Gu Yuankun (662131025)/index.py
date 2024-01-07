import pandas as pd
import re

# read csv
# csv_data = pd.read_csv('./spam.csv', header=None, encoding='ISO-8859-1')
csv_data = pd.read_csv('./spam.csv', encoding='ISO-8859-1')
csv_data = csv_data.rename(columns={'Unnamed: 1': 'v2'})

def count_english_words(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return len(words)

def count_english_unique_words(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    unique_words = set(words)
    return len(unique_words)

def total_word_length(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    total_length = sum(len(word) for word in words)
    return total_length

def total_word_unique_length(text):
    words = set(re.findall(r'\b[a-zA-Z]+\b', text))
    total_length = sum(len(word) for word in words)
    return total_length

# How many rows/sample?
# 5572
num_rows = csv_data.shape[0]
print("The number of rows/samples is", num_rows)

# What is the longest sample?
# longest length: 910
# longest content:
# For me the love should start with attraction.i should feel that I need her every time around me.she should be the first thing which comes in my thoughts.I would start the day and end it with her.she should be there every time I dream.love will be then when my every breath has her name.my life should happen around her.my life will be named to her.I would cry for her.will give all my happiness and take all her sorrows.I will be ready to fight with anyone for her.I will be in love when I will be doing the craziest things for her.love will be when I don't have to proove anyone that my girl is the most beautiful lady on the whole planet.I will always be singing praises for her.love will be when I start up making chicken curry and end up makiing sambar.life will be the most beautiful then.will get every morning and thank god for the day because she is with me.I would like to say a lot..will tell later..
max_length = csv_data['v2'].str.len().max()
longest_content = csv_data.loc[csv_data['v2'].str.len().idxmax(), 'v2']

# print("The longest sample length is", max_length)
print("The longest content sample is", longest_content)

# How many word?
# The words have 85047
# The unique words have 78253
word_count = csv_data['v2'].apply(count_english_words).sum()
word_unique_count = csv_data['v2'].apply(count_english_unique_words).sum()

print("The word has", word_count)
print("The unique word has", word_unique_count)

# What is the average word length?
# The average word length is 3.786741448845932
# The average unique word length is 3.8836977496070437
word_lengths = csv_data['v2'].apply(total_word_length).sum()
average_word_length = word_lengths / word_count

word_unique_lengths = csv_data['v2'].apply(total_word_unique_length).sum()
average_unique_word_length = word_unique_lengths / word_unique_count

print("The average word length is", average_word_length)
print("The average unique word length is", average_unique_word_length)
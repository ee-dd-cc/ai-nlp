import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

csv_data = pd.read_csv('./spam.csv', encoding='ISO-8859-1')

# delete Unnamed column
csv_data = csv_data.loc[:, ~csv_data.columns.str.contains('^Unnamed')]
csv_data = csv_data[['v1', 'v2']]
csv_data.columns = ['label', 'text']
# clear space
def clearSpace(text):
  pattern = re.compile(r'\s+')
  sentence = re.sub(pattern, ' ', text.lower())
  return sentence.strip()

# remove anything that is not English
def removeEnglish(text):
  pattern = re.compile(r'^[a-zA-Z]+$')
  stop_words = set(stopwords.words('english'))
  word_tokens = word_tokenize(text)
  filtered_list = [w for w in word_tokens if not w in stop_words]
  filtered_list = [w for w in filtered_list if pattern.match(w)]
  # return filtered_list
  return ' '.join(filtered_list)

def clearSentence(text):
  space_text = clearSpace(text)
  filtered_list = removeEnglish(space_text)
  return filtered_list

# Create new column name “text2” and "length"
csv_data['text2'] = csv_data['text'].apply(clearSentence)
csv_data['length'] = csv_data['text2'].apply(len)

# print(csv_data)

# 4 Use labelEncoder method to convert class target
label_encoder = LabelEncoder()
for row in csv_data['text2']:
  words_list = row.split(' ')
  encoded_label = label_encoder.fit_transform(words_list)
  # print(encoded_label)

# 5 Use CountVectorize to perform BOW
# vectorizer = CountVectorizer(max_features=10)
vectorizer = CountVectorizer()
bow_transformed = vectorizer.fit_transform(csv_data['text2'])

# Create a DataFrame to show results
bow_df = pd.DataFrame(bow_transformed.toarray(), columns=vectorizer.get_feature_names_out())

# 6 Display the top 5 and bottom 5 rows
top_5 = bow_df.head(5)
bottom_5 = bow_df.tail(5)

print(top_5)
print(bottom_5)

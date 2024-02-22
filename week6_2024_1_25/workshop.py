import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split

csv_data = pd.read_csv('../assets/spam.csv', encoding='ISO-8859-1')

# delete Unnamed column
csv_data = csv_data.loc[:, ~csv_data.columns.str.contains('^Unnamed')]
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
  return ' '.join(filtered_list)

def clearSentence(text):
  space_text = clearSpace(text)
  filtered_list = removeEnglish(space_text)
  return filtered_list

# Preprocess text
docs = csv_data['text'].apply(clearSentence)


# init TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# use the fit_transform transform the docs
X_tfidf = tfidf_vectorizer.fit_transform(docs)

# get feature
feature_list = tfidf_vectorizer.get_feature_names_out()
print('----feature_list counts\n', len(feature_list))

# feature selection and set threshold = 0.001
threshold = 0.001
selector = VarianceThreshold(threshold)
X_selected = selector.fit_transform(X_tfidf)
# selected_features = selector.get_support()
# how many feature you have removed
features_removed = X_tfidf.shape[1] - X_selected.shape[1]
# print('features removed counts: ', len(feature_list) - selected_features.sum())
print(f'features removed counts: {features_removed}')

# stratified hold-out
X_train, X_test, y_train, y_test = train_test_split(
    X_selected, 
    docs, 
    test_size=0.3, 
    random_state=1234, 
    # stratify=docs,
    shuffle=False
)

# train and test
train_shape = X_train.shape
test_shape = X_test.shape

print(train_shape)

# top_10rows
top_10_rows = X_train[:10]
# bottom_10rows
bottom_10_rows = X_train[-10:]
# print('top_10_rows\n', top_10_rows)
# print('bottom_10_rows\n', bottom_10_rows)
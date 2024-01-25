import re

text = '111 Python 222'
# text1 = '09865'

isPy = re.search(r'\bPython\b', text)
print(isPy)
# isPy = re.search('Python', text)

# #[0-9] 匹配第一个数字，确保它在 0 到 9 之间；\d{4} 匹配接下来的四个数字；
# #最后的 \b 确保数字后面是单词边界，即这是一个完整的、独立的五位数数字。
# isPost = re.search(r'\b[0-9]\d{4}\b', text1)

# matches = re.findall(r'\b\d{5}\b', text1)

# # print(isPy)

# print(matches)

# print(isPost)

# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# # import stopwords from nltk.corpus
# sentence = 'Machine learning is cool!'
# stop_words = set(stopwords.words('english'))
# word_tokens = word_tokenize(sentence)
# filtered_sentence = [w for w in word_tokens if not w in stop_words]
# print(filtered_sentence)


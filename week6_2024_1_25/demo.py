import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import train_test_split

# 加载垃圾邮件数据集（替换'spam_data.csv'为您的数据集文件）
csv_data = pd.read_csv('../assets/spam.csv', encoding='ISO-8859-1')
csv_data = csv_data.loc[:, ~csv_data.columns.str.contains('^Unnamed')]
csv_data.columns = ['label', 'text']
# 假设您的数据集具有'text'和'label'列，其中'text'包含文本消息，'label'包含标签（垃圾或非垃圾）。
X = csv_data['text']

tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(X)

# # 设置阈值级别（如0.1所述）
threshold = 0.1
selector = VarianceThreshold(threshold)
X_tfidf_selected = selector.fit_transform(X_tfidf)

# # 报告已移除的特征数量
features_removed = X_tfidf.shape[1] - X_tfidf_selected.shape[1]
print(f"已移除的特征数量：{features_removed}")


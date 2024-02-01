import pandas as pd
import re
import math
from collections import defaultdict

csv_data = pd.read_csv('../assets/spam.csv', encoding='ISO-8859-1')

csv_data = csv_data.loc[:, ~csv_data.columns.str.contains('^Unnamed')]
csv_data.columns = ['label', 'text']

print(csv_data)
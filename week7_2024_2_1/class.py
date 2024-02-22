import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# Load the data from the provided image
data = {
    'Height': [158, 158, 158, 160, 160, 163, 163, 163, 160, 163, 165, 165, 165, 168, 168, 168, 170, 170, 170],
    'Weight': [58, 59, 63, 59, 60, 60, 61, 61, 64, 64, 61, 62, 65, 62, 63, 66, 63, 64, 68],
    'Size': ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', np.nan]
}

df = pd.DataFrame(data)

# Normalize the data
scaler = MinMaxScaler()
df[['Height', 'Weight']] = scaler.fit_transform(df[['Height', 'Weight']])

# Separate the data into train and test sets
train_data = df.dropna()
test_data = df[df['Size'].isna()]

# Train KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_data[['Height', 'Weight']], train_data['Size'])

# Predict the missing size
predicted_size = knn.predict(test_data[['Height', 'Weight']])
predicted_size_label = predicted_size[0]

# Add the prediction to the dataframe
df.loc[df['Size'].isna(), 'Size'] = predicted_size_label

# Plot the data
plt.figure(figsize=(10, 6))
markers = {'L': 'X', 'M': 'o'}
for size, marker in markers.items():
    d = df[df['Size'] == size]
    plt.scatter(d['Height'], d['Weight'], label=f'Size {size}', marker=marker)

# Highlight the predicted point
predicted_point = test_data.iloc[0]
plt.scatter(predicted_point['Height'], predicted_point['Weight'], 
            color='red', label='Predicted Size', marker='s')
plt.title('Normalized Heights and Weights by Size')
plt.xlabel('Normalized Height')
plt.ylabel('Normalized Weight')
plt.legend()
plt.grid(True)
plt.show()

# Show the result
print(predicted_size_label)

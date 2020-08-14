import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from joblib import load

kmeans =load('/Users/edward/Desktop/CELL/algorithm/k_means/kmeans.joblib')
mat = np.load('/Users/edward/Desktop/CELL/algorithm/k_means/km.npy')

y = np.array([[1, 1, 0.5, 1, 0.5, 1, 0, 0.5, 1, 0.5]])
group = kmeans.predict(y)
print(group)

# cosine similarity
# find phones with the same group
cell = (mat[:,-1]==group)

cell_raw = {}
for c in range(23):
    if mat[c,-1]==group:
        x = mat[c,:-2]
        X = x.reshape(1, 10)
        Y = y.reshape(1, 10)
        cos_lib = cosine_similarity(X, Y)
        cell_raw[mat[c,-2]] = (cos_lib[0][0])
    else:
        pass


p = pd.read_csv('/Users/edward/Desktop/CELL/cell_Index/cell_Index.csv', encoding='ANSI')
for n, i in enumerate(sorted(cell_raw.keys())):
    if n<3:
        print(p['Name'][i])
    else:
        pass
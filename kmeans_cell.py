from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from joblib import dump

path ='/Users/edward/Desktop/CELL/matrix/npy/'
fileName = os.listdir(path)
mat = np.array([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])

for n, fn in enumerate(fileName):

    # read npy
    #X = np.load(path + fn)
    #print(X)

    # read npy
    X = np.load(path + fn)

    # append the array of each article
    if n == 0:
        mat = np.append([mat], [X], axis=0)
    else:
        mat = np.append(mat, [X], axis=0)



# K-Means
mat = mat[1:]  # delete the first column with 9s
#print(mat[0][0])
print(mat.shape)


kmeans = KMeans(n_clusters=2, random_state=0, init='k-means++').fit(mat[:,:-1])
pred = np.asmatrix(kmeans.predict(mat[:,:-1]))   #gives X the # of clusters it belongs to
pred = pred.T
print(pred)
print(pred.shape)


# save to npy
model = np.concatenate((mat, pred), axis=1)
print(model)
np.save('/Users/edward/Desktop/CELL/algorithm/k_means/km', model)

# save kmeans model
model = model[:,:-2]       #delete cell phone id and kmeans result
kmeans = KMeans(n_clusters=2, random_state=0, init='k-means++').fit(model)
dump(kmeans, '/Users/edward/Desktop/CELL/algorithm/k_means/kmeans.joblib')


'''
# save to dataframe
df = pd.DataFrame()
df2 = {"ID": id, "Matrix": mat}
df = df.append(df2, ignore_index=True)
df.to_csv('C:/Users/Big data/PycharmProjects/CELL/algorithm/k_means/km.csv')
'''
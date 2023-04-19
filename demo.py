import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import copy
from scipy.linalg import svd, diagsvd

def randomiza_item_matriz(A):
    B = copy.deepcopy(A)
    while True:
        r_i = random.randint(0,len(A)-1)
        r_j = random.randint(0,len(A[r_i])-1)
        if (A[r_i][r_j])!=0:
            r_v = random.randint(0,10)
            B[r_i,r_j] = r_v
            return B, (r_i,r_j)

def estima_valor1(X, s, Y):
    s[200:] *= 0 # VALOR DE K
    S = X @ diagsvd(s, df_.shape[0], df_.shape[1]) @ Y
    return S

def estima_valor2(X, s, Y):
    s[100:] *= 0 # VALOR DE K
    S = X @ diagsvd(s, df_.shape[0], df_.shape[1]) @ Y
    return S

def estima_valor3(X, s, Y):
    s[10:] *= 0 # VALOR DE K
    S = X @ diagsvd(s, df_.shape[0], df_.shape[1]) @ Y
    return S

df = pd.read_csv('ratings_small.csv')
df = df.loc[:, df.columns != 'timestamp']

df_ = pd.pivot_table(data = df, index = 'userId', columns ='movieId', values = 'rating',aggfunc='mean')
df_ = (df_.fillna(0)).to_numpy()
df_.shape 

for i in range(1000):
    B, pos = randomiza_item_matriz(df_)   
    X, s, Y = np.linalg.svd(B)
    S = estima_valor1(X,s,Y)
    D = estima_valor2(X,s,Y)
    E = estima_valor3(X,s,Y)

    print(df_[pos])
    print(S[pos])
    print(D[pos])
    print(E[pos])
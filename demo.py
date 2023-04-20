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

df = pd.read_csv('ratings_small.csv')
df = df.loc[:, df.columns != 'timestamp']

A = pd.pivot_table(data = df, index = 'userId', columns ='movieId', values = 'rating',aggfunc='mean')
A = (A.fillna(0)).to_numpy()
A.shape 


U,s,vt = np.linalg.svd(A)

plt.figure()
plt.plot(s)
plt.show()

def estima_valor(X, s, Y,K):
    s[K:] *= 0 
    S = X @ diagsvd(s, A.shape[0], A.shape[1]) @ Y
    return S

erros = []
for i in range(1000):
    B, pos = randomiza_item_matriz(A)
    X, s, Y = np.linalg.svd(B)
    S = estima_valor(X,s,Y,200)

    erro = A[pos] - S[pos]
    erros.append(erro)

erros = pd.DataFrame(erros)
erros.to_csv('erros.csv', index=False)

dfe=pd.read_csv("erros.csv")
dfe['erros'].mean()

dfe['erros'].hist()

# # Teste de Stress

erros = []
for i in range(1):
    B = A
    posicoes = []
    for i in range(1000):
        B, pos = randomiza_item_matriz(B)
        posicoes.append(pos)

    X, s, Y = np.linalg.svd(B)
    S = estima_valor(X,s,Y,200)
    for pos in posicoes:
        erro = A[pos] - S[pos]
        erros.append(erro)

# erros = pd.DataFrame(erros)
# erros.to_csv('errosStress1000.csv', index=False)

dfe1000 = pd.read_csv('errosStress1000.csv')
print(dfe1000.mean())
dfe1000.hist()

# # Teste de Stress

erros = []
for i in range(1):
    B = A
    posicoes = []
    for i in range(int(100004/2)):
        B, pos = randomiza_item_matriz(B)
        posicoes.append(pos)

    X, s, Y = np.linalg.svd(B)
    S = estima_valor(X,s,Y,200)
    for pos in posicoes:
        erro = A[pos] - S[pos]
        erros.append(erro)

erros = pd.DataFrame(erros)
erros.to_csv(f'errosStress{int(100004/2)}.csv', index=False)

dfef50002 = pd.read_csv(f'errosStress{int(100004/2)}.csv')
dfef50002.hist()

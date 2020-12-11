'''
c = input().split(' ')
N = int(c[0])
M = int(c[1])
B = [[0 for i in range(M)] for j in range(N)]
A = []
H = 0
for i in range(N):
    A = input().split()
    for j in range(M):
        B[i][j] = int(A[j])
for i in range(N):
    for j in range(M):
        if B[i][j] > H:
            H = B[i][j]
k = 0
V = 0
for i in range(N):
    for j in range(M):
        if B[i][j] < -5:
            k += 1
        if B[i][j] < 0:
            V += abs(B[i][j])
print(k)
print(V)
print(H)
'''
'''
import numpy as np
A = np.loadtxt(input())
b = np.loadtxt(input())
X = input().split()
x = np.zeros(len(X))
for i in range(len(X)):
	x[i] = float(X[i])
A2 = A.dot(A)
x1 = x.dot(A2)
x2 = x1.dot(b)
print(x2)
'''
'''
import pandas as pd
df1 = pd.read_csv(input(), sep=';')
df2 = pd.read_csv(input(), sep=';')
df3 = df2.groupby('id').mean().round(3)
dfres = pd.merge(df1, df3, left_on='id', right_on='id')
dfR = dfres.sort_values('mark', ascending=False)
dfRRR = dfR[['name', 'mark']]
dfRRR = dfRRR.reset_index(drop=True)
for i in range(3):
	dfRRR.loc[i,'mark'] = "{0:.3f}".format(dfRRR.loc[i,'mark'])
for i in range(3):
	print(dfRRR.loc[i,'name'], dfRRR.loc[i, 'mark'])
dflast = dfR[dfR['mark'] > 8.0].groupby('company').count().sort_values('mark', ascending=False).iloc[0, :]
sas = dflast.loc['mark']
print(dflast.name, sas)
'''
import pandas as pd
papers = pd.read_csv(input(), sep=';')
links = pd.read_csv(input(), sep=';')
skolko = links.groupby('reference').count()
j = pd.merge(papers, skolko, left_on='title', right_on='reference')
print(skolko)
print(j)
kolvo = papers.groupby('author').count()
print(kolvo)
res0 = pd.merge(j, kolvo, left_on='author', right_on='author')
print(res0)
for i in range


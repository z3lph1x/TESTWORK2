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
print(round(x2, 9))
'''
import pandas as pd
'''
import numpy as np
'''
df1 = pd.read_csv('games001.csv', sep=';')
df2 = pd.read_csv('rates001.csv', sep=';')
print(df1)
df3 = df2.groupby('id').sum()
print(df3)
num = len(df1.index)
a = []
c = [0 for i in range(num)]
b = [0 for i in range(num)]
for i in range(num):
    a.append(i+1)
for i in range(len(df2.index)):
    for j in range(num):
        if df2.loc[i, 'id'] == a[j]:
            b[j] += 1
print(b)
for i in range(1,num+1):
    c[i-1] = df3.loc[i, 'mark']/b[i-1]
print(c)
f = [a, c]
d = sorted(f, key=lambda x: x[1])
print(d)
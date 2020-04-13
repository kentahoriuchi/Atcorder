# -*- coding: utf-8 -*-
n = int(input())
A = list(map(int,(input().split())))
B = list(map(int,(input().split())))
C = list(map(int,(input().split())))
S = 0
before = 100

for i in range(n):
    S += B[A[i]-1]
    if A[i]-1 == before + 1:
        S += C[before]
    before = A[i]-1

print(S)
    

import numpy as np

W = int(input())
N,K = list(map(int, input().split()))
A,B = [],[]
for _ in range(N):
    a,b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

#dp[何番目まで][枚数][幅]
dp = [[[0]*(W+1)]*(K+1) for _ in range(N+1)]
dp = np.array(dp)


for j in range(N):
    for k in range(1,min(j+1,K+1)):
        dp[j+1][k][:A[j]] = dp[j][k][:A[j]]
            
        dp[j+1][k][A[j]:] = np.maximum(dp[j][k-1][:-A[j]] + B[j],dp[j][k][A[j]:])

print(np.max(dp))




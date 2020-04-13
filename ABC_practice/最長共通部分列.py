import numpy as np
n = int(input())
a,b = [],[]
for _ in range(n):
    A = input()
    B = input()
    a.append(A)
    b.append(B)

answer = []

for i in range(n):
    dp = [[0]*len(a[i]) for _ in range(len(b[i]))]
    for j in range(len(b[i])):
        for k in range(len(a[i])):
            if j == 0 or k == 0:
                if a[i][k] == b[i][j]:
                    dp[j][k] += 1
            else:
                if a[i][k] == b[i][j]:
                    dp[j][k] = dp[j-1][k-1] + 1
                else:
                    dp[j][k] = max(dp[j-1][k],dp[j][k-1])
    answer.append(np.max(dp))

for i in range(len(answer)):
    print(answer[i])

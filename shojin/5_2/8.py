N = int(input())
A = list(map(int, input().split()))

dp = [[0]*21 for _ in range(N-1)]

dp[0][A[0]] = 1

for i in range(N-2):
    for j in range(21):
        if j-A[i+1] >=0:
            dp[i+1][j] += dp[i][j-A[i+1]]
        if j+A[i+1] <= 20:
            dp[i+1][j] += dp[i][j+A[i+1]]

print(dp[N-2][A[-1]])
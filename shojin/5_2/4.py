N,W = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
    for j in range(W+1):
        if j-v[i-1][1] >= 0:
            dp[i+1][j] = max(dp[i][j],dp[i][j-v[i-1][1]]+v[i-1][0])
        else:
            dp[i+1][j] = dp[i][j]

print(dp[N][W])


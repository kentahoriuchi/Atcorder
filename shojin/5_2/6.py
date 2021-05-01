n,m = map(int, input().split())
c = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(m+1)]
c.sort()
inf = float('inf')
for i in range(n+1):
    dp[0][i] = inf
    dp[1][i] = i

for j in range(1,m):
    for i in range(n+1):
        if i-c[j] >= 0:
            dp[j+1][i] = min(dp[j][i],dp[j+1][i-c[j]]+1)
        else:
            dp[j+1][i] = dp[j][i]

print(dp[m][n])

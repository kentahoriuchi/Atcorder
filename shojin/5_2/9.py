N,K = map(int, input().split())
d = []
p = []
for _ in range(K):
    a,b = list(map(int, input().split()))
    d.append(a)
    p.append(b)

dp = [[0]*6 for _ in range(N+1)]
dp[1][0] = 1
dp[1][2] = 1
dp[1][4] = 1

for i in range(1,N):
    S = sum(dp[i])
    if i in d:
        pasta = p[d.index(i)]
        if pasta == 1:
            dp[i+1][0] = (S - dp[i][0] - dp[i][1])%10000
            dp[i+1][1] = dp[i][0]%10000
        elif pasta == 2:
            dp[i+1][2] = (S - dp[i][2] - dp[i][3])%10000
            dp[i+1][3] = dp[i][2]%10000
        elif pasta == 3:
            dp[i+1][4] = (S - dp[i][4] - dp[i][5])%10000
            dp[i+1][5] = dp[i][4]%10000
    else:
        dp[i+1][0] = (S - dp[i][0] - dp[i][1])%10000
        dp[i+1][1] = dp[i][0]%10000
        dp[i+1][2] = (S - dp[i][2] - dp[i][3])%10000
        dp[i+1][3] = dp[i][2]%10000
        dp[i+1][4] = (S - dp[i][4] - dp[i][5])%10000
        dp[i+1][5] = dp[i][4]%10000

print(sum(dp[N])%10000)

            
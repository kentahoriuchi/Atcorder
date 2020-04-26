N = int(input())
A = list(map(int, input().split()))
A = [[a,i] for a,i in zip(A,range(N))]
A = sorted(A,reverse=True)

dp = [[0]*(N+1) for _ in range(N+1)]
ans = 0

for n in range(0,N+1):
    for y in range(0,n+1):
        x = n-y
        a = A[n-1]
        ind = a[1]
        if x==0 and y==0:
            dp[x][y] = 0
        elif x==0:
            dp[x][y] = dp[x][y-1] + a[0]*abs(ind-((N-1)-(y-1)))
        elif y==0:
            dp[x][y] = dp[x-1][y]+a[0]*abs(ind-(x-1))
        else:
            dp[x][y] = max(dp[x-1][y]+a[0]*abs(ind-(x-1)),dp[x][y-1] + a[0]*abs(ind-((N-1)-(y-1))))
        ans = max(ans,dp[x][y])

print(ans)
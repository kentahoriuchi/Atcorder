from fractions import gcd
K = int(input())
ans = 0
dp = [0]*201

for i in range(1,K+1):
    for j in range(1,K+1):
        S = 0
        n = gcd(i,j)
        if dp[n] != 0:
            ans += dp[n]
        else:
            for k in range(1,K+1):
                S += gcd(k,n)
            ans += S
            dp[n] = S

print(ans)


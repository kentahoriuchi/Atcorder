from fractions import gcd
N,K = list(map(int, input().split()))

S = [0]*(K+1)
ans = [0]*(K+1)

for i in range(K):
    n = K - i
    yakusu = K//n
    s = pow(yakusu,N,1000000007)
    for j in range(2*n,K+1,n):
        s -= S[j]
    S[n] = s%1000000007
    ans[n] = s*n%1000000007



print(sum(ans)%1000000007)


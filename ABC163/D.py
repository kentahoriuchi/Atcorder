N,K = list(map(int, input().split()))
mod = 10**9+7
ans = 0

for i in range(K,N+2):
    M = N*(N+1)/2 - (N-i)*(N-i+1)/2+1
    m = i*(i-1)/2
    ans += (M-m)%mod

print(int(ans)%mod)
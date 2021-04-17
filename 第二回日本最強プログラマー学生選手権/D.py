N,P = list(map(int, input().split()))
mod = 10**9+7

print(((P-1)*pow(P-2,N-1,mod))%mod)

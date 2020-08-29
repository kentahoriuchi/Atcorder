import sys
K = int(input())
S = input()
mod = 10**9+7

if N == 1:
    print(M)
    sys.exit()

def cmbinit(n):
    fac = [0]*n
    finv = [0]*n
    inv = [0]*n
    fac[0]=fac[1] = 1
    finv[0]=finv[1] = 1
    inv[1] = 1
    for i in range(2,n):
        fac[i] = fac[i-1]*i %mod
        inv[i] = mod - inv[mod%i] * (mod//i) %mod
        finv[i] = finv[i-1] * inv[i]%mod
    
    return fac,finv

def cmb(n,r,fac,finv):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0

    return fac[n] * (finv[r] * finv[n - r] % mod) %mod




ans = 0
fac,finv = cmbinit(N)
for k in range(K+1):
    ans += (M * pow(M-1, N-k-1, mod) * cmb(N-1,k,fac,finv))%mod


print(ans%mod)
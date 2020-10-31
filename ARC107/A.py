A,B,C = list(map(int, input().split()))
mod = 998244353

a = (A*(A+1)//2)%mod
b = (B*(B+1)//2)%mod
c = (C*(C+1)//2)%mod

print((a*b*c)%mod)
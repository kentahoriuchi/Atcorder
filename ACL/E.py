N,Q = list(map(int, input().split()))
L = []
for _ in range(Q):
    L.append(list(map(int, input().split())))

mod = 998244353

n = [str(1)] * N

for j in range(Q):
    n[L[j][0]-1:L[j][1]] = str(L[j][2])*(L[j][1]-L[j][0]+1)
    print(int(''.join(n))%mod)

N,M = list(map(int, input().split()))
a = []
b = []
c = []
d = []
for _ in range(N):
    A,B = list(map(int, input().split()))
    a.append(A)
    b.append(B)
for _ in range(M):
    C,D = list(map(int, input().split()))
    c.append(C)
    d.append(D)
inf = float('inf')

for i in range(N):
    ans = 0
    l = inf
    for j in range(M):
        if l > abs(a[i]-c[j]) + abs(b[i]-d[j]):
            l = abs(a[i]-c[j]) + abs(b[i]-d[j])
            ans = j+1
    print(ans)

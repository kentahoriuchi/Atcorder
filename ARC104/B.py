N,S = list(input().split())
N = int(N)

a = [0]*(N+1)
t = [0]*(N+1)
c = [0]*(N+1)
g = [0]*(N+1)

for i in range(N):
    a[i+1] = a[i]
    t[i+1] = t[i]
    c[i+1] = c[i]
    g[i+1] = g[i]
    if S[i] == 'A':
        a[i+1] += 1
    elif S[i] == 'T':
        t[i+1] += 1
    elif S[i] == 'C':
        c[i+1] += 1
    elif S[i] == 'G':
        g[i+1] += 1


ans = 0

for i in range(N):
    for j in range(i+1,N+1):
        A = a[j]-a[i]
        T = t[j]-t[i]
        C = c[j]-c[i]
        G = g[j]-g[i]
        if A == T and C == G:
            ans += 1

print(ans)
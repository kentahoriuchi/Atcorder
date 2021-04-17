N,M = list(map(int, input().split()))
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 0
for t1 in range(M-1):
    for t2 in range(t1+1,M):
        s = 0
        for n in range(N):
            s += max(A[n][t1],A[n][t2])
        ans = max(ans,s)

print(ans)
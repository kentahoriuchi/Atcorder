N,M,K= list(map(int, input().split()))
C = []
A = []
for _ in range(N):
    c= list(map(int, input().split()))
    C.append(c[0])
    A.append(c[1:])
inf = float('inf')
ans = inf

for i in range(2**N):
    re = [0]*M
    count = 0
    for j in range(N):
        if((i>>j)&1):
            count += C[j]
            for k in range(M):
                re[k] += A[j][k]
    
    flag = True
    for n in range(M):
        if re[n] < K:
            flag = False
    
    if flag:
        ans = min(ans,count)

if ans == inf:
    print(-1)
else:
    print(ans)

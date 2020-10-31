N,K = list(map(int, input().split()))
if K < 0:
    K = -K
li = []

for i in range(2,2*N):
    if i+K <= 2*N:
        li.append([i+K,i])
    else:
        break
if K == 0:
    li.append([2*N,2*N])

def kosu(n,N):
    if n%2 == 0:
        if n-1 <= N:
            m = (n-1 - n//2 +1) * 2-1
        else:
            m = (N - n//2 +1) * 2-1
    else:
        if n-1 <= N:
            m = (n-1- (n+1)//2 +1)*2
        else:
            m = (N- (n+1)//2 +1)*2
    
    return m

ans = 0
for k in li:
    ans += kosu(k[0],N)*kosu(k[1],N)

print(ans)
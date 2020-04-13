N,M = list(map(int, input().split()))
n = [0]*(N+1)
for _ in range(M):
    a,b = list(map(int, input().split()))
    n[a] += 1
    n[b] += 1


flag = True
for j in range(len(n)):
    if n[j]%2 != 0:
        flag = False

if flag:
    print('YES')
else:
    print('NO')




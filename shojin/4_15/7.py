N,M = list(map(int, input().split()))
s = []
for _ in range(M):
    s.append(list(map(int, input().split())))
p = list(map(int, input().split()))

ans = 0

for i in range(2**N):
    tentou = 0
    for j in range(M):
        swi = 0
        for k in range(s[j][0]):
            if ((i >> s[j][k+1]-1) & 1):
                swi += 1
        if swi % 2 == p[j]:
            tentou += 1
    if tentou == M:
        ans += 1

print(ans)

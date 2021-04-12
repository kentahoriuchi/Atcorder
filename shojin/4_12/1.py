N = int(input())
x = []
for _ in range(N):
    x.append(list(map(int, input().split())))
kyori = []

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            kyori.append([x[i][0]-x[j][0],x[i][1]-x[j][1]])
# print(kyori)
ans = 0
for k in kyori:
    s = 0
    for l in kyori:
        if k == l:
            s += 1
    ans = max(s,ans)

print(N-ans)


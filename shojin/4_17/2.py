R,C = list(map(int, input().split()))
c = []
for _ in range(R):
    c.append(list(map(int, input().split())))

ans = 0
for i in range(2**R):
    kari = 0
    li = [[0 for _ in range(C)] for _ in range(R)]
    for j in range(R):
        if ((i >> j) & 1):
            for p in range(len(c[j])):
                if c[j][p] == 1:
                    li[j][p] = 0
                else:
                    li[j][p] = 1
        else:
            li[j] = c[j]
    for k in range(C):
        count = 0
        for l in range(R):
            if li[l][k] == 1:
                count += 1
        kari += max(count,R-count)
    ans = max(kari,ans)

print(ans)

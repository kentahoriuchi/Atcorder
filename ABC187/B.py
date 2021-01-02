N = int(input())
x = []
for _ in range(N):
    x.append(list(map(int, input().split())))

ans =0
for i in range(N):
    for j in range(i+1,N):
        if (x[j][1] - x[i][1]) / (x[j][0] - x[i][0]) >= -1 and (x[j][1] - x[i][1]) / (x[j][0] - x[i][0]) <= 1 :
            ans += 1

print(ans)
N,D = list(map(int, input().split()))
X = [[0]*D for _ in range(N)]
for j in range(N):
    x = list(map(int, input().split()))
    for i in range(D):
        X[j][i] = x[i]




count =0

for i in range(N):
    for j in range(i+1,N):
        n = 0
        for k in range(D):
            n += (X[i][k] - X[j][k])**2
        n_d = int(n**0.5)**2
        if n == n_d:
            count += 1
print(count)
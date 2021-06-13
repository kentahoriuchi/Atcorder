H,W = list(map(int, input().split()))
C = [[0]*(H+1) for _ in range(W+1)]
for i in range(1,H+1):
    c = list(map(int, input().split()))
    for j in range(W):
        C[j+1][i] = c[j]


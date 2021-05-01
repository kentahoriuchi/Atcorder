N,D,H = list(map(int, input().split()))
d = []
for _ in range(N):
    d.append(list(map(int, input().split())))

min_katamuki = 10**8
for i in range(N):
    kata = (H-d[i][1])/(D-d[i][0])
    min_katamuki = min(min_katamuki,kata)

if H - min_katamuki*D <= 0:
    print(0.0)
else:
    print(H - min_katamuki*D)
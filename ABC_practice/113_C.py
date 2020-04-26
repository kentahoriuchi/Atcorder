
N,M = list(map(int, input().split()))
P = []
Y = []
for _ in range(M):
    p,y = list(map(int, input().split()))
    P.append(p)
    Y.append(y)
count = [0]*(N+1)
ans = [0]*(M+1)
data = [[p,y,i] for p,y,i in zip(P,Y,range(1,M+1))]

data.sort(key=lambda x: x[1])

for i in range(M):
    count[data[i][0]] += 1
    ans[data[i][2]] = count[data[i][0]]


for j in range(1,M+1):
    a = P[j-1]
    b = ans[j]
    print(str(a*(10**6)+b).zfill(12))





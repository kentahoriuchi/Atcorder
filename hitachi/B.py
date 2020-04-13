A,B,M = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = []
for _ in range(M):
    x,y,c = list(map(int, input().split()))
    m.append([x,y,c])

nedan = min(a)+min(b)
for j in range(M):
    nedan = min(nedan,a[m[j][0]-1]+b[m[j][1]-1]-m[j][2])

print(nedan)



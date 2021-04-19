from itertools import permutations
import math
N = int(input())
x = []
for _ in range(N):
    x.append(list(map(int, input().split())))

li=range(N)
per=permutations(li,N)
ans = 0
count = 0
for i in per:
    count += 1
    pre = [0,0]
    for j in range(len(i)):
        if j == 0:
            n = i[j]
            pre = [x[n][0],x[n][1]]
        else:
            n = i[j]
            ans += math.sqrt((x[n][0]-pre[0])**2+(x[n][1]-pre[1])**2)
            pre = [x[n][0],x[n][1]]

print(ans/count)

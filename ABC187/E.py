from collections import deque
N = int(input())
x = []
for _ in range(N-1):
    x.append(list(map(int, input().split())))
Q = int(input())
y = []
for _ in range(Q):
    y.append(list(map(int, input().split())))

path = [[] for i in range(N)]
ans = [0] * N

for i in range(len(x)):
    path[x[i][0]-1].append(x[i][1]-1)
    path[x[i][1]-1].append(x[i][0]-1)

for j in range(Q):
    score = y[j][2]
    if y[j][0] == 1:
        root = x[y[j][1]-1][0]-1
        ng = x[y[j][1]-1][1]-1
    else:
        root = x[y[j][1]-1][1]-1
        ng = x[y[j][1]-1][0]-1
    stack = deque(path[root])
    ans[root] += score
    visited = [root]
    pre = root
    while stack:
        nex = stack.pop()
        if nex == ng:
            continue
        else:
            ans[nex] += score
            for i in path[nex]:
                if not i in visited:
                    stack.appendleft(i)
        visited.append(nex)

for j in range(N):
    print(ans[j])
        




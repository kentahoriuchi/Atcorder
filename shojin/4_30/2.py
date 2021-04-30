from collections import deque

N,Q = list(map(int, input().split()))
path = [[0]*N for _ in range(N)]
for _ in range(N-1):
    tmp = list(map(int, input().split()))
    path[tmp[0]-1][tmp[1]-1] = 1
    path[tmp[1]-1][tmp[0]-1] = 1
ans = [0]*N
dic = [0]*N
for _ in range(Q):
    tmp = list(map(int, input().split()))
    dic[tmp[0]-1] += tmp[1]

visited = [0]*N

point = 0
stack = deque([0])
while stack:
    u = stack.pop()
    visited[u] = 1
    ans[u] += point
    ans[u] += dic[u]
    point = ans[u]
    for k in range(len(path[u])):
        if path[u][k] == 1 and visited[k] != 1:
            stack.append(k)


print(' '.join(map(str,ans)))



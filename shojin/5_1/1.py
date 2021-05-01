from collections import deque
n = int(input())
V = []
for _ in range(n):
    u,_,*v = list(map(int, input().split()))
    V.append(v)

distance = [-1]*n
stack = deque([1])
count = 0
visited = [False]*n
        
def bfs(x):
    count = 0
    Q = deque([])
    C = deque([])
    global visited
    global distance
    visited[x-1] = True
    Q.appendleft(x)
    C.appendleft(count)
    while Q:
        q = Q.pop()
        c = C.pop()
        distance[q-1] = c
        for l in V[q-1]:
            if visited[l-1] == False:
                visited[l-1] = True
                Q.appendleft(l)
                C.appendleft(c+1)

bfs(1)

for i in range(n):
    print(i+1,distance[i])



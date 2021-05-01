from collections import deque
H,W,N = list(map(int, input().split()))
maze = []
num = ['1','2','3','4','5','6','7','8','9']
goal = [[0,0] for _ in range(N)]
maze = [['X' for _ in range(W+2)]]
hp = 1
for i in range(H):
    li = list(input())
    if 'S' in li:
        start = [i+1,li.index('S')+1]
    for l in num:
        if l in li:
            goal[int(l)-1] = [i+1,li.index(l)+1]
    maze.append(['X']+li+['X'])
maze.append(['X' for _ in range(W+2)])
inf = float('inf')

def bfs(sy,sx,gy,gx):
    visited = [[inf]*(W+2) for _ in range(H+2)]
    stack = deque([[sy,sx]])
    visited[sy][sx] = 0
    while stack:
        y,x = stack.pop()
        p = visited[y][x]
        if y == gy and x == gx:
            return p
        for j,k in ([1,0],[0,1],[-1,0],[0,-1]):
            new_y,new_x = y+j,x+k
            if maze[new_y][new_x] != 'X' and visited[new_y][new_x] == inf:
                visited[new_y][new_x] = p+1
                stack.appendleft([new_y,new_x])

ans = 0
done = [i for i in range(1,N+1)]
while done:
    k = []
    kouho = []
    for r in done:
        if r > hp:
            continue
        else:
            sc = bfs(start[0],start[1],goal[r-1][0],goal[r-1][1])
            k.append(r)
            kouho.append(sc)
    ans += min(kouho)
    ind = k[kouho.index(min(kouho))]
    done.remove(ind)
    hp += 1
    start = [goal[ind-1][0],goal[ind-1][1]]

print(ans)

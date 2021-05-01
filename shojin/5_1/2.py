from collections import deque

R,C = list(map(int, input().split()))
sy,sx = list(map(int, input().split()))
gy,gx = list(map(int, input().split()))
c = []
for _ in range(R):
    c.append(list(input()))

def bfs(sy,sx,gy,gx):
    stack = deque([[sy,sx]])
    path = deque([0])
    visited = [[False]*C for _ in range(R)]
    visited[sy][sx] = True
    while stack:
        y,x = stack.pop()
        p = path.pop()
        if y == gy and x == gx:
            return p
        
        for j,k in ([1,0],[0,1],[-1,0],[0,-1]):
            new_y,new_x = y+j,x+k
            if c[new_y][new_x] == '.' and visited[new_y][new_x] == False:
                visited[new_y][new_x] = True
                stack.appendleft([new_y,new_x])
                path.appendleft(p+1)

print(bfs(sy-1,sx-1,gy-1,gx-1))
        
        

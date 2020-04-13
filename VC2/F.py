from collections import deque

H,W = list(map(int, input().split()))
maze = [input() for _ in range(W)]

def dfs(maze,visited,sx,sy,gx,gy):
    stack = deque([[sy,sx]])
    visited[sy][sx] = 1
    while stack:
        y,x = stack.pop()
        color = maze[y][x]
        count = visied[y][x] 
        if y == gy and x == gx:
            return 1
        
        for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
            new_y,new_x = y+j,x+k
            if new_x < 0 or new_x >= W or new_y < 0 or new_y >= H:
                continue
            #深さ優先
            elif maze[new_y][new_x] != color and visited[new_y][new_x] > count+1:
                visited[new_y][new_x] = count+1
                stack.append([new_y, new_x])

inf = float('inf')
visited = [[inf]*H for _ in range(W)]

ans = 0
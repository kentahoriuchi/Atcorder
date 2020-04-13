from collections import deque

R,C = list(map(int, input().split()))
sy,sx = list(map(int, input().split()))
gy,gx = list(map(int, input().split()))
maze = [input() for _ in range(R)]

def bfs(maze,visited,sx,sy,gx,gy):
    stack = deque([[sy,sx]])
    visited[sy][sx] = 0
    while stack:
        y,x = stack.pop()
        count = visited[y][x]
        if x == gx and y == gy:
            return count
            break
        
        for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
            new_y,new_x = y+j,x+k
            if new_x < 0 or new_x >= C or new_y < 0 or new_y >= R:
                continue
            #深さ優先
            elif maze[new_y][new_x] != "#" and visited[new_y][new_x] > count+1:
                visited[new_y][new_x] = count+1
                stack.appendleft([new_y, new_x])

inf = float('inf')
visited = [[inf]*C for _ in range(R)]
print(bfs(maze,visited,sx-1,sy-1,gx-1,gy-1))




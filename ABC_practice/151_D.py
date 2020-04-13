from collections import deque

H,W = list(map(int, input().split()))
maze = [input() for _ in range(H)]
answer = 0

def bfs(maze,visited,sx,sy):
    stack = deque([[sy,sx]])
    visited[sy][sx] = 0
    while stack:
        y,x = stack.pop()
        count = visited[y][x]
        
        for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
            new_y,new_x = y+j,x+k
            if new_x < 0 or new_x >= W or new_y < 0 or new_y >= H:
                continue
            #深さ優先
            elif maze[new_y][new_x] != "#" and visited[new_y][new_x] > count+1:
                visited[new_y][new_x] = count+1
                stack.appendleft([new_y, new_x])
    return count

inf = float('inf')

for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            visited = [[inf]*W for _ in range(H)]
            answer = max(answer,bfs(maze,visited,j,i))
print(answer)



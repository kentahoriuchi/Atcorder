from collections import deque

H,W = list(map(int, input().split()))
maze = [input() for _ in range(H)]

def bfs(maze,visited,gx,gy):
    stack = deque([[0,0]])
    if maze[0][0] == '#':
        visited[0][0] = 1 
    else:
        visited[0][0] = 0 
    while stack:
        y,x = stack.pop()
        count = visited[y][x]
        
        for j,k in ([1,0],[0,1]):
            new_y,new_x = y+j,x+k
            if  new_x >= gx or  new_y >= gy:
                continue
            elif maze[new_y][new_x] == "#" and maze[y][x] == '.' and visited[new_y][new_x] > count+1:
                visited[new_y][new_x] = count+1
                stack.appendleft([new_y, new_x])
            elif maze[new_y][new_x] == "#" and maze[y][x] == '.' and visited[new_y][new_x] <= count+1:
                continue
            elif visited[new_y][new_x] > count:
                visited[new_y][new_x] = count
                stack.appendleft([new_y, new_x])
    return visited[gy-1][gx-1]

inf = float('inf')
visited = [[inf]*W for _ in range(H)]
print(bfs(maze,visited,W,H))

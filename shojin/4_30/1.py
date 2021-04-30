from collections import deque
import sys

while True:
    w,h = list(map(int, input().split()))
    if w == 0 and h == 0:
        break
        sys.exit()
    c = []
    for _ in range(h):
        c.append(list(map(int, input().split())))

    visited = [[0]*w for _ in range(h)]
    islands = 0


    def dfs(i,j):
        stack = deque([[i,j]])
        while stack:
            x,y = stack.pop()
            if c[x][y] == 0 or visited[x][y] == 1:
                continue
            visited[x][y] = 1
            if x-1>=0 and y-1>=0:
                if c[x-1][y-1] == 1:
                    stack.append([x-1,y-1])
            if x-1>=0:
                if c[x-1][y] == 1:
                    stack.append([x-1,y])
            if x-1>=0 and y+1<=w-1:
                if c[x-1][y+1] == 1:
                    stack.append([x-1,y+1])
            if y+1<=w-1:
                if c[x][y+1] == 1:
                    stack.append([x,y+1])
            if x+1<=h-1 and y+1<=w-1:
                if c[x+1][y+1] == 1:
                    stack.append([x+1,y+1])
            if x+1<=h-1:
                if c[x+1][y] == 1:
                    stack.append([x+1,y])
            if x+1<=h-1 and y-1>=0:
                if c[x+1][y-1] == 1:
                    stack.append([x+1,y-1])
            if y-1>=0:
                if c[x][y-1] == 1:
                    stack.append([x,y-1])

        

    for i in range(h):
        for j in range(w):
            if c[i][j] == 1 and visited[i][j] != 1:
                dfs(i,j)
                islands += 1
    print(islands)
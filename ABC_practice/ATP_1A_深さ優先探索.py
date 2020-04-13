from collections import deque

H,W = list(map(int, input().split()))
maze = [input() for _ in range(H)]

def dfs(maze,visited,sh,sw):
    stack = deque([[sh,sw]])
    visited[sh][sw] = 1
    while stack:
        #print(stack)
        h,w = stack.pop()
        if maze[h][w] == 'g':
            return 'Yes'
        
        for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
            new_h,new_w = h+j,w+k
            if new_h < 0 or new_h >= H or new_w < 0 or new_w >= W:
                continue
            #深さ優先
            elif maze[new_h][new_w] != "#" and visited[new_h][new_w] == 0:
                visited[new_h][new_w] = 1
                stack.append([new_h, new_w])
    
    return 'No'

#スタート位置検索
for i in range(H):
    if maze[i].find('s') != -1:
        sh = i
        sw = maze[i].find('s')
        break

#通った箇所記録
visited = [[0]*W for _ in range(H)]
print(dfs(maze,visited,sh,sw))



from collections import deque
H,W = map(int, input().split())
s = [['#']+list(input())+['#'] for _ in range(H)]
s = [['#']*(W+2)] + s + [['#']*(W+2)]

num = 0
for l in s:
    num += l.count('.')

flag = False
inf = float('inf')
stack = deque([[1,1]])
visited = [[inf]*(W+2) for _ in range(H+2)]
visited[1][1] = 1
while stack:
    y,x = stack.pop()
    path = visited[y][x]
    if y == H and x == W:
        flag = True
        break

    for j,k in ([1,0],[0,1],[-1,0],[0,-1]):
        new_y,new_x = y+j,x+k
        if s[new_y][new_x] == '.' and visited[new_y][new_x] == inf:
            visited[new_y][new_x] = path + 1
            stack.appendleft([new_y,new_x])
    
if flag:
    print(num-path)
else:
    print(-1)

from collections import deque
N = int(input())
p = list(map(int, input().split()))

seat = [[1]*(N+1) for i in range(N+1)]

stack = deque(p)

while stack:
  s = stack.pop()
  y = (s-1)//N+1
  x = s%N
  seat[(x-1)//N+1][x%N] = 0
  count = 0

  for j,k in ([1,0],[-1,0],[0,1],[0,-1]):
            new_y,new_x = y+j,x+k
            if new_x < 0 or new_x >= C or new_y < 0 or new_y >= R:
                continue
            #深さ優先
            elif maze[new_y][new_x] != "#" and visited[new_y][new_x] > count+1:
                visited[new_y][new_x] = count+1
                stack.appendleft([new_y, new_x])



from collections import deque
m = int(input())
n = int(input())
c = []
c.append([0 for _ in range(m+2)])
for _ in range(n):
    t = [0]+list(map(int, input().split()))+[0]
    c.append(t)
c.append([0 for _ in range(m+2)])
max_depth = 0

def dfs(table,x,y,depth):
    global max_depth
    table[x][y] = 0
    if table[x-1][y] == 1:
        dfs(table,x-1,y,depth+1)
    if table[x][y-1] == 1:
        dfs(table,x,y-1,depth+1)
    if table[x+1][y] == 1:
        dfs(table,x+1,y,depth+1)
    if table[x][y+1] == 1:
        dfs(table,x,y+1,depth+1)
    table[x][y] = 1

    if table[x-1][y] == 0 and table[x][y-1] == 0 and table[x+1][y] == 0 and table[x][y+1] == 0:
        max_depth = max(max_depth,depth+1)

for i in range(1,m+1):
    for j in range(1,n+1):
        if c[j][i] == 1:
            dfs(c,j,i,0)
print(max_depth)
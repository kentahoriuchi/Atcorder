from collections import deque
W, H = map(int, input().split())
a = [[0] + list(map(int, input().split())) + [0] for _ in range(H)]
a = [[0]*(W+2)] + a + [[0]*(W+2)]
directions = [[(-1,-1),(0,-1),(1,0),(0,1),(-1,1),(-1,0)],[(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,0)]]
 
ans = 0
q = deque()
q.append((0, 0))
a[0][0] = -1
while q:
    x, y = q.popleft()
    for d in directions[y%2]:
        x2 = x + d[0]
        y2 = y + d[1]
        if 0 <= x2 <= W+1 and 0 <= y2 <= H+1:
            if a[y2][x2] == 1:
                ans += 1
            if a[y2][x2] == 0:
                a[y2][x2] = -1
                q.append((x2, y2))
print(ans)
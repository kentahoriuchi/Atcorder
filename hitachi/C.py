from collections import deque
from itertools import combinations

N = int(input())
road = set([])
for i in range(N-1):
    a,b = list(map(int, input().split()))
    road.add((a,b))
    road.add((b,a))

inf = float('inf')
three_set = set([])
for j in range(N):
    visit = [inf]*N
    stack = deque([j+1])
    visit[j] = 0
    while stack:
        print(stack)
        x = stack.pop()
        count = visit[x-1]
        if count == 3:
            break

        for r in road:
            r = list(r)
            if r[0] == x and visit[r[1]-1] == inf:
                visit[r[1]-1] = count+1
                if visit[r[1]-1] == 3:
                    if j+1 < r[1]:
                        three_set.add((j+1,r[1]))
                stack.appendleft(r[1])

N_list = [i for i in range(N)]
comb = set(combinations(range(N),2))



    
    



from itertools import permutations
N = int(input())
r = []
for _ in range(N):
    r.append(list(map(int, input().split())))

def naname(l):
    masu = []
    now = [l[0],l[1]]
    while now[0] >= 1 and now[1] >= 1:
        masu.append([now[0]-1,now[1]-1])
        now = [now[0]-1,now[1]-1]
    now = [l[0],l[1]]
    while now[0] >= 1 and now[1] <= 6:
        masu.append([now[0]-1,now[1]+1])
        now = [now[0]-1,now[1]+1]
    now = [l[0],l[1]]
    while now[0] <= 6 and now[1] >= 1:
        masu.append([now[0]+1,now[1]-1])
        now = [now[0]+1,now[1]-1]
    now = [l[0],l[1]]
    while now[0] <= 6 and now[1] <= 6:
        masu.append([now[0]+1,now[1]+1])
        now = [now[0]+1,now[1]+1]
    return masu

li=range(8)


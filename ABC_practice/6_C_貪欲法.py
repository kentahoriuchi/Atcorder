from collections import deque

N = int(input())
W = deque([])
for _ in range(N):
    w = int(input())
    W.appendleft(w)

now = []

for j in range(N):
    weight = W.pop()
    now.sort()
    if now == []:
        now.append(weight)
    elif max(now) < weight:
        now.append(weight)
    else:
        for i in range(len(now)):
            if now[i] >= weight:
                now[i] = weight
                break

print(len(now))



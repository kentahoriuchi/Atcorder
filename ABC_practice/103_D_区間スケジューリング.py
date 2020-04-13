N,M = list(map(int, input().split()))
S = []
for _ in range(M):
    A,B = list(map(int, input().split()))
    S.append([A,B])
S = sorted(S, key=lambda x:x[1])

rem = 0
now = 0

for ab in S:
    left = ab[0]
    right = ab[1]
    if left <= now:
        continue
    else:
        now = right -1
        rem += 1

print(rem)
from bisect import bisect
N,M = list(map(int, input().split()))
P = []
for _ in range(N):
    P.append(int(input()))

P.append(0)

p2 = []
for i in range(len(P)):
    for j in range(len(P)):
        p2.append(P[i]+P[j])
p2.sort()

ans = 0
for k in p2:
    if k > M:
        break
    # left = 0
    # right = len(p2)-1
    # while left < right:
    #     mid = (left+right)//2
    #     if p2[mid] == M - k:
    #         ans = M
    #         break
    #     elif p2[mid] < M - k:
    #         left = mid + 1
    #     else:
    #         right = mid
    right = bisect(p2,M-k)
    ans = max(ans,p2[right-1]+k)

print(ans)
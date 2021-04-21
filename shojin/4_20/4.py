N = int(input())
H = []
S = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    H.append(tmp[0])
    S.append(tmp[1])

height_max = 10**14
height_min = 0

def shageki(H,S,h):
    nissu = []
    for i in range(len(H)):
        nissu.append((h-H[i])/S[i])
    nissu.sort()
    for j in range(len(nissu)):
        if nissu[j] < j:
            return -1
    return 0


left = height_min
right = height_max
while left < right:
    mid = (left + right) // 2
    if shageki(H,S,mid) == 0:
        right = mid
    elif shageki(H,S,mid) == -1:
        left = mid+1

if shageki(H,S,mid) == -1:
    print(mid+1)
else:
    print(mid)



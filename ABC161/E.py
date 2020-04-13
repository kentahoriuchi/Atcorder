import copy
N,K,C = list(map(int, input().split()))
S = list(input())
mae = [0]*K
ushiro = [0]*K
hi = 0
youso = 0

while True:
    if S[hi] == 'o':
        mae[youso] = hi+1
        youso += 1
        if youso == K:
            break
        hi += C
    hi += 1

hi = N-1
youso = 0

while True:
    if S[hi] == 'o':
        ushiro[youso] = hi+1
        youso += 1
        if youso == K:
            break
        hi -= C
    hi -= 1
ushiro.reverse()

for j in range(len(mae)):
    if mae[j] == ushiro[j]:
        print(mae[j])










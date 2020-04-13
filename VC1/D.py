import math
N = int(input())
S = []
ans = 0
count = 1
for _ in range(N):
    s = list(input())
    s.sort()
    S.append(''.join(s))
S.sort()
S.append('a')

for i in range(N):
    if S[i] == S[i+1]:
        count += 1
    else:
        if count > 2:
            ans += math.factorial(count)//(math.factorial(count-2)*math.factorial(2))
        elif count == 2:
            ans += 1
        count =1

print(ans)
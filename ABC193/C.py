import math
N = int(input())
l = [0]*int(math.sqrt(N)+1)
ans = 0

for i in range(2,int(math.sqrt(N)+1)):
    if l[i] == 0:
        for k in range(2,50):
            if i**k <= int(math.sqrt(N)):
                l[i**k] = 1
                ans += 1
            elif i**k <= N:
                ans += 1
            else:
                break

print(N-ans)

import sys
A,B,C,X,Y = list(map(int, input().split()))

ans = float('inf')

C = 2*C

for i in range(10**5+1):
    s = C * i
    if X > i:
        s += A*(X-i)
    if Y > i:
        s += B*(Y-i)
    
    ans = min(ans,s)

print(ans)
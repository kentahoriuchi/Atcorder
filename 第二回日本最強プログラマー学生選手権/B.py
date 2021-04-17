N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = []

for i in range(1,1001):
    if i in A and i in B:
        continue
    elif i in A or i in B:
        ans.append(str(i))

print(' '.join(ans))


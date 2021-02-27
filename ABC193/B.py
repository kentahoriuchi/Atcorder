N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

ans = 10**10
for i in range(len(A)):
    if A[i][2]-A[i][0] > 0:
        ans = min(ans,A[i][1])

if ans == 10**10:
    print(-1)
else:
    print(ans)
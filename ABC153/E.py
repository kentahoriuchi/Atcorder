H,N = list(map(int, input().split()))
A = []
B = []
for _ in range(N):
    a,b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

dp = [float('inf') for i in range(H+max(A))]
dp[0] = 0

for i in range(H+max(A)):
    for j in range(N):
        if i-A[j] >= 0:
            dp[i] = min(dp[i-A[j]]+B[j],dp[i])

print(min(dp[H:]))



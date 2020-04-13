N = int(input())
a = list(map(int, input().split()))

ans = 1000000000

a_min = min(a)
a_max = max(a)

for i in range(a_min,a_max+1):
    S = 0
    for j in range(N):
        S += (a[j]-i)**2
    ans = min(S,ans)

print(ans)

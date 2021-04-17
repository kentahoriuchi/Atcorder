N,K = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = float('inf')
for i in range(2**N):
    cost = 0
    height = a[0]
    n = 1
    for j in range(1,N):
        if ((i >> j) & 1):
            n += 1
            if a[j] > height:
                height = a[j]
            else:
                cost += height - a[j] + 1
                height += 1
        else:
            height = max(height,a[j])
        # print(cost)
    if n >= K:
        ans = min(cost,ans)

print(ans)


N = int(input())

ans = 0
for i in range(1,N+1):
    yaku = 0
    for j in range(1,i+1):
        if i % j == 0:
            yaku += 1
    if yaku == 8 and i % 2==1:
        ans += 1

print(ans)
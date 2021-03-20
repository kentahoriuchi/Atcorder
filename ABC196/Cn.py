N = int(input())
ans = 0
for i in range(1,100001):
    s = str(i)
    s = int(s+s)
    if s > N:
        ans = i-1
        break

print(ans)

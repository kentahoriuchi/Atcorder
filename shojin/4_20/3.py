N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

from bisect import bisect, bisect_left, bisect_right
 
ans = 0
for i in range(N):
    num_a = bisect_left(a, b[i])
    num_c = N - bisect_right(c, b[i])
    ans += num_a * num_c
print(ans)


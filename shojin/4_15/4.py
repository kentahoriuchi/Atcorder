n = int(input())
x = []
y = []
for _ in range(n):
   X,Y = list(map(int, input().split()))
   x.append(X)
   y.append(Y)

x.sort()
y.sort()

ans = 0
for i in range(1,len(x)//2+1):
    ans += x[-1*i] - x[i-1]
    ans += y[-1*i] - y[i-1]
for l in range(n):
    ans += y[l] -x[l]

print(ans)
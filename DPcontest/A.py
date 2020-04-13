N = int(input())
h = list(map(int, input().split()))

cost = [0]*N+[10000]

for i in range(1,N):
    cost[i] = min(cost[i-1]+abs(h[i-1]-h[i]),cost[i-2]+abs(h[i-2]-h[i]))

print(cost[N-1])
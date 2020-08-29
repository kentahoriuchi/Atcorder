N,H,R = list(map(int, input().split()))
h = []
c = []
for _ in range(N):
    C = list(map(int, input().split()))
    h.append(C[0])
    c.append(C[1])

L = []
for i in range(N):
    for j in range(i+1,N):
        L.append(h[j]-h[i])

L = list(set(L))
L.sort()
inf = float('inf')
ans = inf
for kyori in L:
  cost = c[0]
  count = 1
  ichi = 0
  flag = False
  while ichi < H:
    for j in range(N):
      if h[j] > ichi+kyori:
        ichi = h[j-1]+kyori
        count += 1
        cost += c[j-1]
        break
      if j == N-1:
        flag = True
    if flag:
      break
  cost += count * kyori
  ans = min(ans,cost)

print(ans)
  

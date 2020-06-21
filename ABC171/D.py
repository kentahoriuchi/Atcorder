N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = []
for _ in range(Q):
  B.append(list(map(int, input().split())))


d = [0]*(10**5+1)
ans = 0
for i in range(N):
  d[A[i]] += 1
  ans += A[i]

for j in range(Q):
  ans = ans - d[B[j][0]]*B[j][0] + d[B[j][0]]*B[j][1]
  d[B[j][1]] += d[B[j][0]]
  d[B[j][0]] = 0
  print(ans)

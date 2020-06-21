N = int(input())
a = list(map(int, input().split()))

S = 0
for i in range(N):
  S = S^a[i]

for j in range(N):
  print(S^a[j])
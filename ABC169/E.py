N = int(input())
A = []
B = []
for _ in range(N):
  a,b = list(map(int, input().split()))
  A.append(a)
  B.append(b)

A.sort()
B.sort()

if N%2 != 0:
  print(B[(N+1)//2-1]-A[(N+1)//2-1]+1)
else:
  print(int((((B[(N)//2-1]+B[(N)//2])/2)-((A[(N)//2-1]+A[(N)//2])/2))*2+1))


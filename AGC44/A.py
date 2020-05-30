T = int(input())
C = []
for _ in range(T):
  a = list(map(int, input().split()))
  C.append(a)


def cost(n,C):
  A = C[0]/n
  B = C[1]/(2*n)
  c = C[2]/(4*n)
  D = C[3]
  return A,B,c,D

cost = 0
while(k*5 < N):
  ind = cost(k,C).index(min(cost(k,C)))
  if ind == 0:
    cost += C[0]
    k = 2*k
  elif ind == 1:
    cost += C[1]
    k = 3*k
  elif ind == 2:
    cost += C[2]
    k = 5*k

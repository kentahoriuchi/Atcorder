N = int(input())
A = list(map(int, input().split()))

A.sort()
prime = []

while A:
  p = A[0]
  if p > max(A)//2:
    break
  if len(A) >= 2 and A[0] == A[1]:
    A = [e for e in A if e % p != 0]
  else:
    prime.append(p)
    A = [e for e in A if e % p != 0]

de = []
for i in range(len(A)-1):
  if A[i] == A[i+1]:
    de.append(A[i])
de = de + list(set(de))
for j in de:
  A.remove(j)


print(len(prime)+len(A))



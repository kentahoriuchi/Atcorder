N,M,V,P = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort(reverse=True)
score = A[P-1]

B = list(map(lambda  x: x+M, A))
n = sum(x>=score for x in B)
print(n)

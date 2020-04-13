N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)

S = sum(A)/(4*M)

if A[M-1] >= S:
    print('Yes')
else:
    print('No')


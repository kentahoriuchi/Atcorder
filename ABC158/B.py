N,A,B = list(map(int, input().split()))

n = N//(A+B)
if N-n*(A+B) > A:
    print((n+1)*A)
else:
    print(n*A+N-n*(A+B))
N,A,B = list(map(int, input().split()))

if (B-A)%2 == 0:
    print(((B-A)//2))
else:
    n = min(A-1,N-B)
    print(n+(B-A+1)//2)

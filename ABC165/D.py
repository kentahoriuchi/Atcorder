A,B,N =  list(map(int, input().split()))


if N < B-1:
    print(A*N//B)
else:
    print(A*(B-1)//B)
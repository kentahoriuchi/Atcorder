N,M =  list(map(int, input().split()))
if N % 2!=0:
    for i in range(1,M+1):
        print(i,N-i+1)
else:
    d = []
    for i in range(1,M+1):
        if i in d:
            print(i,N-i)
        else:
            print(i,N-i+1)
            d.append(N//2-i+1)



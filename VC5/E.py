N = int(input())
count = 0
if N ==2:
    print(1)
else:

    for i in range(2,int((N-1)**0.5)+1):
        if (N-1)%i == 0:
            count += 1
            if (N-1)//i != i:
                count += 1

    for j in range(2,int(N**0.5)+1):
        if N%j == 0:
            n = N
            while n%j == 0:
                n = n//j
            if n%j == 1:
                count += 1
            if N//j != j:
                n = N
                while n%(N//j) == 0:
                    n = n//(N//j)
                if n%(N//j) == 1:
                    count += 1
    print(count+2)


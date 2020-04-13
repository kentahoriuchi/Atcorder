import math
N = int(input())
if N == 2:
    print(1)
else:
    ans = [N-1,N]

    #N-1
    for i in range(2,int(math.sqrt(N-1)+1)):
        if (N-1) % i == 0:
            ans.append(i)
            if i != (N-1)//i:
                ans.append((N-1)//i)

    #N
    for j in range(2,int(math.sqrt(N))+1):
        if N % j == 0:
            n1 = N
            n2 = N
            while n1 % j == 0:
                n1 = n1/j
            if n1 % j == 1:
                ans.append(j)
            if j != N//j:
                while n2 % N//j == 0:
                    n2 = n2*j//N
                if n2 % j == 1:
                    ans.append(N//j)
        
    print(len(ans))
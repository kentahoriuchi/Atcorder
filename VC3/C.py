N = int(input())

for i in range(1,N+1):
    if i*(i+1) < 2*N:
        continue
    else:
        for j in range(1,i+1):
            if j == i*(i+1)//2 - N:
                continue
            print(j)
        break
N,Y = list(map(int, input().split()))
a = [-1,-1,-1]

while(True):
    for i in range(N+1):
        for j in range(N-i+1):
            if 10000*i + 5000*j + 1000*(N-i-j) == Y:
                a[0] = i
                a[1] = j
                a[2] = N-i-j
                break
    break

print(' '.join([str(n) for n in a]))

        
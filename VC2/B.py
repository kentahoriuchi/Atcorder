R,G,B,N = list(map(int, input().split()))
count = 0

for i in range(int(N/R)+1):
    for j in range(int((N-i*R)/G)+1):
        if (N-i*R-j*G)%B == 0:
            count += 1

print(count)
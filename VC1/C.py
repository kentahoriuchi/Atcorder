N = int(input())

for i in range(1,N+1):
    if i*(i+1) >= 2*N:
        n = i
        break

for j in range(1,n+1):
    if j == ((i*(i+1)//2)-N):
        continue
    print(j)
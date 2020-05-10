N,K= list(map(int, input().split()))
A= list(map(int, input().split()))

path = [0]*N
a = 0

for j in range(N+1):
    count = j
    a = A[a]-1
    if path[a]!= 0:
        b = path[a]
        c = j+1-path[a]
        break
    else:
        path[a] = j+1

mod = (K-b)%c

if count > K:
    print(path.index(K)+1)
else:
    print(path.index(mod+b)+1)

    


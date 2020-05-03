N,M =  list(map(int, input().split()))
H =  list(map(int, input().split()))
A = []
for i in range(M):
    a =  list(map(int, input().split()))
    A.append(a)



ans = [1] * N

for l in range(M):
    if H[A[l][0]-1] > H[A[l][1]-1]:
        ans[A[l][1]-1] = 0
    elif H[A[l][0]-1] == H[A[l][1]-1]:
        ans[A[l][1]-1] = 0
        ans[A[l][0]-1] = 0
    else:
         ans[A[l][0]-1] = 0

print(sum(ans))

N,M = list(map(int, input().split()))
A = list(map(int, input().split()))
a = []

for i in range(N):
    for j in range(N):
        a.append(A[i]+A[j])
a.sort(reverse=True)
print(sum(a[:M]))
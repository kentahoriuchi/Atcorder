N = int(input())
A = list(map(int, input().split()))
n = [0]*(N)

for i in range(N-1):
    n[A[i]-1] += 1

for i in range(len(n)):
    print(n[i])
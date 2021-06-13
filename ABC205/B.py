import sys
N = int(input())
A = list(map(int, input().split()))

A.sort()
for i in range(1,N+1):
    if int(A[i-1]) != i:
        print('No')
        sys.exit()

print('Yes')
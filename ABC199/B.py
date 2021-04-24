N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = max(A)
m = min(B)

if m-M+1 >= 0:
    print(m-M+1)
else:
    print(0)

N = int(input())
A = list(input().split())

if len(A) == len(list(set(A))):
    print('YES')
else:
    print('NO')
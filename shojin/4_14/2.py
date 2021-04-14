A,B = list(map(int, input().split()))

a = max(A,B)
b = min(A,B)

if (a-b)%2 == 0:
    print((a+b)//2)
else:
    print('IMPOSSIBLE')
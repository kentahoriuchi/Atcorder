A,B = list(map(int, input().split()))

a = str(A)
b = str(B)
a = int(a[0]) + int(a[1]) + int(a[2])
b = int(b[0]) + int(b[1]) + int(b[2])

if a >= b:
    print(a)
else:
    print(b)
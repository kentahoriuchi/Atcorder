A,B,W = list(map(int, input().split()))

W = W * 1000

a = W/A
b = W/B

a = int(a)
if b != int(b):
    b = int(b)+1
else:
    b = int(b)


if a >= b:
    print(b,a)
else:
    print('UNSATISFIABLE')
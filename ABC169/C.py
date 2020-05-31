from decimal import *

A,B= list(input().split())
B = Decimal(B)
A = int(A)
ans = A*B

print(int(ans))
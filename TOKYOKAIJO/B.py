A,V = list(map(int, input().split()))
B,W = list(map(int, input().split()))
T = int(input())

L = abs(A-B)
v = V-W

if v*T >= L:
  print('YES')
else:
  print('NO')
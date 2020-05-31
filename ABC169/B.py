N = int(input())
A = list(map(int, input().split()))
k = 0 in A
flag = True
ans = 1
if k:
  print(0)
else:
  for i in range(N):
    ans *= A[i]
    if ans > 10**18:
      flag = False
      break

  if flag:
    print(ans)
  else:
    print(-1)
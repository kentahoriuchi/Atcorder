N = int(input())
A= list(map(int, input().split()))
S = sum(A)
ans = 0
leaf = 1
S_now = 0

if A[0] == 1:
  if N==0:
    print(1)
  else:
    print(-1)
elif A[0] != 0:
  print(-1)
else:
  for i in range(N):
    ans += leaf
    leaf -= A[i]
    S_now += A[i] 
    leaf = min(leaf*2,S-S_now)
  if A[-1] != leaf:
    print(-1)
  else:
    print(ans+A[-1])
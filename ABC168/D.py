from collections import deque
N,M = list(map(int, input().split()))
ab = deque([[] for i in range(N+1)])
for _ in range(M):
  A= list(map(int, input().split()))
  ab[A[0]].append(A[1])
  ab[A[1]].append(A[0])

ans = [0]*(N+1)
done = [0]*(N+1)
done[0]=1
done[1]=1

stack = deque([1])

while stack:
  x = stack.pop()
  temp = deque([])
  for i in ab[x]:
    if done[i] == 0:
      done[i] += 1
      ans[i] = x
      stack.appendleft(i)

print('Yes')
for i in range(2,len(ans)):
  print(ans[i])



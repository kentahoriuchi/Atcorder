from collections import deque
K = int(input())

stack = deque([9,8,7,6,5,4,3,2,1])
count = 0

while stack:
    n = stack.pop()
    count += 1
    if count == K:
        print(n)
        break
    if n%10 != 0:
        stack.appendleft(n*10+n%10-1)
    
    stack.appendleft(n*10+n%10)

    if n%10 != 9:
        stack.appendleft(n*10+n%10+1)
    




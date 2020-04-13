from collections import deque
N = int(input())
alpha = ['a','b','c','d','e','f','g','h','i','j']
ans = []

stack = deque(['a'])

while stack:
    if len(stack[-1]) == N:
        break
    s = stack.pop()
    s_list = sorted(list(s))
    index = alpha.index(s_list[-1])
    for i in range(index+2):
        stack.appendleft(s+alpha[i])
    

stack.reverse()
for j in range(len(stack)):
    print(stack[j])


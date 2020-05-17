ans = [0]*(N+1)
# done = [0]*(N+1)
# done[0]=1
# done[1]=1

# stack = deque([1])

# while stack:
#   x = stack.pop()
#   temp = deque([])
#   for i in range(len(ab)):
#     c = ab.pop()
#     if x in c:
#       if c[0] == x:
#         if done[c[1]] == 0:
#           done[c[1]]+=1
#           stack.appendleft(c[1])
#           ans[c[1]] = x
#       else:
#         if done[c[0]] == 0:
#           done[c[0]] +=1
#           stack.appendleft(c[0])
#           ans[c[0]] = x
#     else:
#       temp.append(c)  
#   ab = temp

# print('Yes')
# for i in range(2,len(ans)):
#   print(ans[i])

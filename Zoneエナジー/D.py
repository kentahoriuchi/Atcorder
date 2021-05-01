
from collections import deque

S = list(input())
T = deque([])
flag = False
for i in range(len(S)):
    if S[i] == 'R':
        flag = not flag
    else:
        if not flag:
            if T and T[-1] == S[i]:
                T.pop()
            else:
                T.append(S[i])
        else:
            if T and T[0] == S[i]:
                T.popleft()
            else:
                T.appendleft(S[i])


# ans = deque([])
# for l in range(len(T)):
#     if len(ans) > 0:
#         if T[l] == ans[-1]:
#             _ = ans.pop()
#             continue
#     ans.append(T[l])

if flag:
    T.reverse()
    

print(''.join(T))

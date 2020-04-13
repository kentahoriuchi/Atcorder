S = list(input())
T = list(input())

s_reversed = list(reversed(S))
T_reversed = list(reversed(T))
F = 0

for i in range(len(S)-len(T)+1):
    s = s_reversed[i:i+len(T)]
    flag = 0
    for j in range(len(T)):
        if s[j] == T_reversed[j] or s[j] == '?':
            continue
        else:
            flag += 1
            break
    if flag ==0:
        F += 1
        for j in range(len(T)):
            s_reversed[i+j] = T_reversed[j]
        break

if F ==0:
    print('UNRESTORABLE')
else:
    R = ''.join(list(reversed(s_reversed)))
    print(R.replace('?','a'))




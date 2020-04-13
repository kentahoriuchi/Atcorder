S = list(input())
T = list(input())

S.reverse()
T.reverse()
flag = False

for i in range(len(S)-len(T)+1):
    for j in range(len(T)):
        if S[j+i] == T[j] or S[j+i] == '?':
            pass
        else:
            break

        if j == len(T)-1:
            flag = True
            for k in range(len(T)):
                if S[k+i] == '?':
                    S[k+i] = T[k]
            break
    if flag:
        break

if flag:
    for i in range(len(S)):
        if S[i] == '?':
            S[i] = 'a'
    S.reverse()
    print(''.join(S))

else:
    print('UNRESTORABLE')




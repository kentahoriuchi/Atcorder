N = int(input())
S = list(input())
Q = int(input())
T = []
for _ in range(Q):
    T.append(list(map(int, input().split())))

def irekae(S,flag,t):
    if flag == 0:
        tmp = S[t[2]-1]
        S[t[2]-1] = S[t[1]-1]
        S[t[1]-1] = tmp
    else:
        if t[2] <= N:
            t[2] = t[2] + N
        else:
            t[2] = t[2] - N
        if t[1] <= N:
            t[1] = t[1] + N
        else:
            t[1] = t[1] - N
        tmp = S[t[2]-1]
        S[t[2]-1] = S[t[1]-1]
        S[t[1]-1] = tmp

    return S

flag = 0
for i in range(Q):
    if T[i][0] == 1:
        S = irekae(S,flag,T[i])
    else:
        if flag == 0:
            flag = 1
        else:
            flag = 0

if flag == 1:
    S = S[N:] + S[:N]
print(''.join(S))

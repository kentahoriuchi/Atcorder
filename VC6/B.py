S = input()
T = input()
l = ['a','t','c','o','d','e','r']
flag = True

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    if S[i] == '@' and T[i] in l:
        continue
    if T[i] == '@' and S[i] in l:
        continue
    flag = False

if flag:
    print('You can win')
else:
    print('You will lose')
    
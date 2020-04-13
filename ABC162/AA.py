N = list(input())
flag = False

for i in range(3):
    if N[i] == '7':
        flag = True

if flag:
    print('Yes')
else:
    print('No')

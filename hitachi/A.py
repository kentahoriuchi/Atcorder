s = list(input())
flag = 0

if len(s)%2 == 1:
    flag = 1
for i in range(len(s)//2):
    if s[2*i] == 'h' and s[2*i+1] == 'i':
        continue
    else:
        flag = 1

if flag == 0:
    print('Yes')
else:
    print('No')

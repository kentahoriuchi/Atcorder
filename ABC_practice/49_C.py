S = list(input())
re = ['dream','dreamer','erase','eraser']
devide = False

T = []

for l in range(len(S)):
    T.insert(0,S.pop(-1))
    if len(T) >= 5:
        if ''.join(T) in re:
            T = []
    if len(T) > 7:
        break

if T == []:
    devide = True

if devide == False:
    print('NO')
else:
    print('YES')



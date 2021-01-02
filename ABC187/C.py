N = int(input())
x = []
for _ in range(N):
    x.append(input())

not_ex = []
ex = []
for i in range(N):
    if x[i][0] == '!':
        ex.append(x[i])
    else:
        not_ex.append(x[i])

ex = list(set(ex))
not_ex = list(set(not_ex))

for i in range(len(ex)):
    ex[i] = ex[i][1:]

ex.extend(not_ex)

if len(ex) == len(list(set(ex))):
    print('satisfiable')
else:
    ex.sort()
    for i in range(len(ex)-1):
        if ex[i] == ex[i+1]:
            print(ex[i])
            break
        

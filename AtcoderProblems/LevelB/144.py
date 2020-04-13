N = int(input())
exist = False

for i in range(1,10):
    for j in range(1,10):
        if i * j == N:
            exist = True

if exist:
    print('Yes')
else:
    print('No')


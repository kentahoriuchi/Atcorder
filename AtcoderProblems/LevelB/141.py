S = input()
easy = True

for i in range(len(S)):
    if i%2 == 0 and S[i] == 'L':
        easy = False
    elif i%2 == 1 and S[i] == 'R':
        easy = False

if easy:
    print('Yes')
else:
    print('No')
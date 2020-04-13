N = int(input())
S = list(input())

if N%2 == 1:
    print('No')

else:
    if S[:N//2] == S[N//2:]:
        print('Yes')
    else:
        print('No')
N = int(input())
S = list(input())

Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in range(len(S)):
    S[i] = Alphabet[(Alphabet.index(S[i])+N)%26]

print(''.join(S))
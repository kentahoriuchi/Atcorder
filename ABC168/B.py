K = int(input())
S = list(input())

if len(S) <= K:
  print(''.join(S))
else:
  print(''.join(S[:K])+'...')
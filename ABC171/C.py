N = int(input())
ans = []

while True:
  if N%26 == 0:
    ans.append('z')
  else:
    ans.append(chr(N%26+96))
  N = (N-1)//26
  if N == 0:
    break
ans.reverse()
print(''.join(ans))


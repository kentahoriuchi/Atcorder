x,n = list(map(int, input().split()))
p = list(map(int, input().split()))

if not x in p:
  print(x)
else:
  for i in range(1,100):
    if not x-i in p:
      print(x-i)
      break
    if not x+i in p:
      print(x+i)
      break


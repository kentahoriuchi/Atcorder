A,B = list(map(int, input().split()))
l = A-B*2

if l < 0:
    print(0)
else:
    print(l)
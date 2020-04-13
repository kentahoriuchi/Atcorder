A,B,C = list(map(int, input().split()))
l = C-(A-B)
if l <= 0:
    print(0)
else:
    print(l)
a,b,x = list(map(int, input().split()))

if a%x ==0 and b%x == 0:
    print(b//x-a//x+1)
elif a%x == 0:
    print(b//x-a//x+1)
elif b%x == 0:
    print(b//x-a//x)
else:
    print(b//x-a//x)

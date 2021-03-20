import math
N = int(input())
keta = math.log10(N)



if keta >= 11:
    print(9+90+900+9000+90000)
elif keta >= 9:
    t = 0
    for i in range(10000,100000):
        if i * 100001 > N:
            break
        else:
            t += 1
    print(9+90+900+9000+t)
elif keta >= 7:
    t = 0
    for i in range(1000,10000):
        if i * 10001 > N:
            break
        else:
            t += 1
    print(9+90+900+t)
elif keta >= 5:
    t = 0
    for i in range(100,1000):
        if i * 1001 > N:
            break
        else:
            t += 1
    print(9+90+t)
elif keta >= 3:
    t = 0
    for i in range(10,100):
        if i * 101 > N:
            break
        else:
            t += 1
    print(9+t)
elif keta >= 1:
    t = 0
    for i in range(1,10):
        if i * 11 > N:
            break
        else:
            t += 1
    print(t)
else:
    print(0)
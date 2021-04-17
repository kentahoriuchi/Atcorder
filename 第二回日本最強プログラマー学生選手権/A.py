X,Y,Z = list(map(int, input().split()))

for i in range(10**7):
    if Y/X <= i/Z:
        print(i-1)
        break
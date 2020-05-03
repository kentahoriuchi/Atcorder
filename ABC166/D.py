import sys
X = int(input())
k = 0

for l in range(1,2*(10**4)):
    a =l
    mod = (a%10-X%10)%10
    for b in range(mod,a+1,10):
        if a**5 - b**5 == X:
            print(a,b)
            sys.exit()
    mod = (X%10-a%10)%10
    for b in range(mod,a+1,10):
        if a**5 + b**5 == X:
            print(a,-b)
            sys.exit()

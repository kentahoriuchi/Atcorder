import math
A,B,X = list(map(int, input().split()))

def nedan(n):
    return A*n + B*int(math.log10(n)+1)

if nedan(1000000000) <= X:
    print(1000000000)
else:
    min = 0
    max = 1000000000
    while(True):
        if nedan((max+min)//2) <= X:
            min = (max+min)//2
        else:
            max = (max+min)//2
        
        if abs(max-min)<=1:
            break

    if nedan(max) <= X:
        print(max)
    else:
        print(min)


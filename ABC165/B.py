X = int(input())
p = 100
i = 0

while(True):
    i += 1
    p = int(p*(1.01))
    if X <= p:
        print(i)
        break

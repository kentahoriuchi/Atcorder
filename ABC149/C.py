X = int(input())
sosu = True
if X == 2:
    print(2)
else:
    while(sosu):
        for i in range(2,X):
            if X%i == 0:
                break
            if i == X-1:
                sosu = False
        if sosu == False: break
        X += 1

    print(X)

A = int(input())
count = 0
N = 1000-A

while(True):
    if N >= 500:
        count += 1
        N -= 500
    else:
        if N >= 100:
            count += 1
            N -= 100
        else:
            if N >= 50:
                count += 1
                N-= 50
            else:
                if N>= 10:
                    count += 1
                    N -= 10
                else:
                    if N>= 5:
                        count += 1
                        N -= 5
                    else:
                        if N>= 1:
                            count += 1
                            N -= 1

    if N == 0:
        break

print(count)  

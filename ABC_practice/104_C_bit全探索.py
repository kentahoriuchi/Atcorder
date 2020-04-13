D,G = list(map(int, input().split()))
P = []
C = []
for i in range(D):
    p,c = list(map(int, input().split()))
    P.append(p)
    C.append(c)
s = {i for i in range(D)}
flag = False
bit = 0
number = []

for bit in range(2**D):
    score = 0
    count = 0
    comp = []
    # print(bit)
    for j in range(D):
        if bit & (1<<j):
            score += P[j] * 100 * (j+1) + C[j]
            count += P[j]
            comp.append(j)
    if score >= G:
        number.append(count)
    else:
        n = max(s-set(comp))
        for k in range(P[n]):
            score += 100 * (n+1)
            count += 1
            if score >= G:
                number.append(count)
                break

print(min(number))

        
                


    



    

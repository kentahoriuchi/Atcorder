S = list(input())

mod = 10**9+7

amari = [0]*13
amari[0] = 1

for i in range(len(S)):
    if S[i] == '?':
        add = range(10)
    else:
        add = [int(S[i])]
    kari = [x for x in amari]
    K = [0]*13
    for l in range(len(kari)):
        for k in add:
            K[(k+l*10)%13] += kari[l] % mod
    amari = [x% mod for x in K]

print(amari[5])

    


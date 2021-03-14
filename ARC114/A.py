N = int(input())
X = list(map(int, input().split()))
ans = 1
sosu = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

S = []
moto = []
for i in range(N):
    yaku = []
    for n in sosu:
        if X[i] % n == 0:
            yaku.append(n)
    if len(yaku) == 1:
        ans = ans * yaku[0]
    else:
        moto.append(X[i])
        S.append(yaku)
        


print(ans)
        

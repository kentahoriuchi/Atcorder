N = int(input())
f = list(map(int, input().split()))

S = 0
for i in range(N):
    if f[i] == i+1:
        S+=1
    else:
        nex = f[i]
        f[i] = 0
        while True:
            if nex == 0:
                break
            elif nex == i+1:
                S+=1
                break
            nex = f[nex-1]
            f[nex-1] = 0

print(pow(2,S,998244353)-1)
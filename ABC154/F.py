
r1,c1,r2,c2 = list(map(int, input().split()))
S = 0

def seki(k):
    c = 1
    for i in range(1,k+1):
        c *= i
    return c
def keiro(r,c):
    return (seki(r+c)%100000007/(seki(r)*seki(c)))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        S += keiro(r1+i,c1+j)

print(S)

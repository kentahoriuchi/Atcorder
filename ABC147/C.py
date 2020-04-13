N = int(input())
X = []
Y = []
count = 0
for j in range(N):
    A = int(input())
    Xj = []
    Yj = []
    for _ in range(A):
        x,y = list(map(int, input().split()))
        Xj.append(x)
        Yj.append(y)
    X.append(Xj)
    Y.append(Yj)

def irekae(l):
    for i in range(l):
        if l(i) == 1:
            l(i) = 0
        else:
            l(i) = 1

for i in range(N):
    for l in range(len(X[i]):
        




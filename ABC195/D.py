N,M,Q = list(map(int, input().split()))
W = []
for _ in range(N):
    W.append(list(map(int, input().split())))
X = list(map(int, input().split()))
for _ in range(Q):
    ans = 0
    w = W[:1]+W[1:]
    q = list(map(int, input().split()))
    x = X[:q[0]-1] + X[q[1]:]
    x.sort()
    for y in x:
        v =list(filter(lambda x: x[0] <= y, w))
        if len(v)!=0:
            v = sorted(v,key=lambda x:x[1])
            # print(w)
            ans += v[-1][1]
            w.remove(v[-1])
    print(ans)

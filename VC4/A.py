N,L = list(map(int, input().split()))
l = []
l_abs = []
for i in range(N):
    l.append(L+i)
    l_abs.append(abs(L+i))


print(sum(l)-l[l_abs.index(min(l_abs))])

N,Q = list(map(int, input().split()))
S = list(input())
l = []
r = []
for _ in range(Q):
    L,R = list(map(int, input().split()))
    l.append(L)
    r.append(R)
flag = False
ac = [0]*N
count = 0

for j in range(N):
        if S[j] == 'A':
            flag = True
            ac[j] = count
            continue
        if S[j] == 'C' and flag:
            count += 1
        ac[j] = count
        flag = False


for i in range(Q):
    print(ac[r[i]-1]-ac[l[i]-1])

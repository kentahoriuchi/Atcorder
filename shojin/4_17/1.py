N,M = list(map(int, input().split()))
x = []
for _ in range(M):
    x.append(list(map(int, input().split())))

ans = 1
for i in range(2**N):
    member = []
    for j in range(N):
        if ((i >> j) & 1):
            member.append(j+1)
    if len(member) == 1:
        continue
    flag = True
    for k in range(len(member)-1):
        for l in range(k+1,len(member)):
            if [member[k],member[l]] not in x:
                flag = False
                break
    if flag:
        ans = max(ans,len(member))

print(ans)



N = int(input())
R = list(map(int, input().split()))

ans = 0
l = [R[0],0]
kai = 1
for i in range(1,N):
    if l[1] == 0:
        if l[0] > R[i]:
            l = [R[i],1]
            kai += 1
        else:
            l = [R[i],0]
    else:
        if l[0] < R[i]:
            l = [R[i],0]
            kai += 1
        else:
            l = [R[i],1]
ans = kai

l = [R[0],1]
kai = 1
for i in range(1,N):
    if l[1] == 0:
        if l[0] > R[i]:
            l = [R[i],1]
            kai += 1
        else:
            l = [R[i],0]
    else:
        if l[0] < R[i]:
            l = [R[i],0]
            kai += 1
        else:
            l = [R[i],1]
ans = max(ans,kai)

if ans >= 3:
    print(ans)
else:
    print(0)

N = int(input())
S = list(input())
ans = 0

for i in range(1000):
    s_an = str(i).zfill(3)
    flag1 = False
    flag2 = False
    flag3 = False
    for s in S:
        if not flag1 and s_an[0] == s:
            flag1 = True
            continue
        if not flag2 and flag1 and s_an[1] == s:
            flag2 = True
            continue
        if not flag3 and flag2 and s_an[2] == s:
            flag3 = True
            continue
    if flag3:
        ans += 1

print(ans)
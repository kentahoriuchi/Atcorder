L = input()
L = list(L.split('><'))
if len(L) == 1:
    a = [L[0].count('<'),L[0].count('>')]
    a_max = max(a)
    ans = a_max*(a_max+1)/2
else:
    ans = 0
    for i in range(len(L)):
        if i == 0:
            a = [L[i].count('<'),L[i].count('>')+1]
        elif i == len(L)-1:
            a = [L[i].count('<')+1,L[i].count('>')]
        else:
            a = [L[i].count('<')+1,L[i].count('>')+1]
        a_max = max(a)
        a_min = min(a)

        ans += a_max*(a_max+1)/2
        ans += a_min*(a_min-1)/2

print(int(ans))

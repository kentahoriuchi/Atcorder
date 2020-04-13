N = int(input())
ans = 0
g = 10

if N%2 != 0:
    print(0)
else:
    flag = True
    while flag:
        i = N//g
        if i == 0:
            break
        ans += i
        g *= 5
    
    print(ans)
        

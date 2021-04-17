n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

for i in m:
    for j in range(2**n):
        flag = True
        s = 0
        for k in range(n):
            if ((j >> k) & 1):
                s += A[k]
        if i == s:
            print('yes')
            flag = False
            break
    if flag: 
        print('no')

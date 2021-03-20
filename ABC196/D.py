H,W,A,B = list(map(int, input().split()))

m = min(H,W)

def kaijo(n):
    k = 1
    for i in range(1,n+1):
        k*=i
    return k

if m == 1:
    print(kaijo(A+B)//(kaijo(A)*kaijo(B)))
elif m == 2:
    

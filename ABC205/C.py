A,B,C = list(map(int, input().split()))

def plus(a,b):
    if a > b:
        print('>')
    elif b > a:
        print('<')
    else:
        print('=')

if A >= 0 and B >= 0:
    plus(A,B)
elif A < 0 and B >= 0:
    if C%2 == 0:
        plus(-A,B)
    else:
        print('<')
elif A>= 0 and B < 0:
    if C%2 == 0:
        plus(A,-B)
    else:
        print('>')
else:
    if C%2 == 0:
        plus(-A,-B)
    else:
        plus(-B,-A)

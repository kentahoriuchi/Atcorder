import math
N = int(input())

l = math.log10(N)

c1 = 10**6-10**3
c2 = 10**9-10**6
c3 = 10**12-10**9
c4 = 10**15-10**12

if l == 15:
    print(c1+c2*2+c3*3+c4*4+5)
elif l >= 12:
    print(c1+c2*2+c3*3+(N-10**12+1)*4)
elif l >= 9:
    print(c1+c2*2+(N-10**9+1)*3)
elif l >= 6:
    print(c1+(N-10**6+1)*2)
elif l >= 3:
    print((N-10**3+1)*1)
else:
    print(0)
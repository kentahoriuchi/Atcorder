import sys
N = int(input())

thres_a = int(19/0.47712125472)
thres_b = int(19/0.69897000433)

for a in range(1,thres_a):
    for b in range(1,thres_b):
        if 3**a + 5**b == N:
            print(a,b)
            sys.exit()

print(-1)
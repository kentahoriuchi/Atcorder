H,W = list(map(int, input().split()))

if H == 1 or W == 1:
    print(1)
elif H*W%2 == 0:
    print(H*W//2)
else:
    print(H*W//2+1)
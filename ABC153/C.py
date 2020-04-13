N,K = list(map(int, input().split()))
H = list(map(int, input().split()))

H.sort(reverse=True)

if len(H) <= K:
    print('0')
else:
    del H[:K]
    print(sum(H)) 

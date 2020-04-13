A,B,K = list(map(int, input().split()))

N = A+B-K

if N <=0:
    print('0 0')
elif N < B:
    print('0 %d' %N)
else:
    print('%d %d' %(A-K,B))
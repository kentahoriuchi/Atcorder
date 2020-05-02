K = int(input())
A,B = list(map(int, input().split()))

for i in range(A,B+1):
    if i % K == 0:
        print('OK')
        break
    if i == B:
        print('NG')
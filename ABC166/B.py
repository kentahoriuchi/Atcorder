N,K =  list(map(int, input().split()))
a = []
sunuke = [0]*N
for i in range(K):
    d = int(input())
    A =  list(map(int, input().split()))
    for l in range(len(A)):
        sunuke[A[l]-1] += 1

print(sunuke.count(0))

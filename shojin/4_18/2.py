from itertools import permutations
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

li=range(1,N+1)
per=permutations(li,N)
count = 0
for i in per:
    i = list(i)
    count += 1
    if i == P:
        a = count
    if i == Q:
        b = count

print(abs(a-b))
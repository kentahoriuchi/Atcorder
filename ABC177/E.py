import fractions
N = int(input())
A = list(map(int, input().split()))

pairwise = True
setwise = False

M = 10**6+1

count = [0 for _ in range(M)]

for a in A:
    count[a] += 1

max_count = 0
for j in range(2,M):
    max_count = max(max_count,sum(count[j::j]))

if max_count == N:
    print('not coprime')
elif max_count >= 2:
    print('setwise coprime')
else:
    print('pairwise coprime')



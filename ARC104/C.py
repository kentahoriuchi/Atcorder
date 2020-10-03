import sys
N = int(input())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    if a[i][0] >= a[i][1]:
        print('No')
        sys.exit()


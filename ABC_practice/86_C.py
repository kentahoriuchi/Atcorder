N = int(input())
T = []
Z = []
time = []
T.append([0,0,0])
for i in range(N):
    t = list(map(int, input().split()))
    T.append(t)
goal = True

for l in range(len(T)-1):
    Z.append(abs(T[l+1][1]-T[l][1]) + abs(T[l+1][2]-T[l][2]))
    time.append(T[l+1][0] - T[l][0])

for j in range(len(T)-1):
    if Z[j] > time[j] or Z[j]%2 != time[j]%2:
        goal = False
        break

if goal == False:
    print('No')
else:
    print('Yes')

 
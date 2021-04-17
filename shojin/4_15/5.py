import sys
m = int(input())
M = []
for _ in range(m):
    M.append(list(map(int, input().split())))
n = int(input())
N = []
for _ in range(n):
    N.append(list(map(int, input().split())))

kijun = M[0]

for i in range(len(N)):
    delta_x = N[i][0] - kijun[0]
    delta_y = N[i][1] - kijun[1]
    flag = True
    for j in range(1,len(M)):
        if [M[j][0]+delta_x,M[j][1]+delta_y] not in N:
            flag = False
            break
    
    if flag:
        print(delta_x,delta_y)
        sys.exit()
    

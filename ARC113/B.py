A,B,C = list(map(int, input().split()))

b_4 = B%4

if b_4 == 0:
    b = 4
elif b_4 == 1:
    b = 1
elif b_4 == 2:
    if C == 1:
        b = 2
    else:
        b = 4
elif b_4 == 3:
    if C %2 == 0:
        b = 1
    else:
        b = 3

ans_d = [[0,0,0,0],[1,1,1,1],[2,4,8,6],[3,9,7,1],[4,6,4,6],[5,5,5,5],[6,6,6,6],[7,9,3,1],[8,4,2,6],[9,1,9,1]]

print(ans_d[A%10][b-1])
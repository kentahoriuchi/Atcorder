A,B = list(map(int, input().split()))
flag = 0

for j in range(1250):
    if int(j*0.08) == A and int(j*0.10) == B:
        print(j)
        flag = 1
        break

if flag == 0:
    print(-1)



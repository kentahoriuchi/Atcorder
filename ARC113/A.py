K = int(input())

cou = 0
niju = 0
ichiju = 0
for A in range(1,K):
    for B in range(A,max((K//A)+1,A+1)):
        for C in range(B,max((K//A//B)+1,B+1)):
            if A * B * C <= K:
                cou += 1
                if A == B and B == C:
                    niju += 1
                elif A == B or B == C or A == C:
                    ichiju += 1

# print(cou,niju,ichiju)
if K == 1:
    print(1)
else:
    ans = (cou -niju - ichiju) * 6 + ichiju * 3 + niju
    print(ans)



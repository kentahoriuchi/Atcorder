n = input().split()
N,K = int(n[0]),int(n[1])
S = list(input())

count = 0
count_s1 = 0
count_sn = 0
s_1 = S[0]
if s_1 == "L":
    count_s1 += 1
s_N = S[-1]
if s_N == "R":
    count_sn += 1

for i in range(len(S)-1):
    if S[i] == "R" and S[i+1] == "L":
        count += 1

if K <= count:
    print(N - ((count-K)*2 + count_s1 + count_sn))
else:
    print(N-1) 


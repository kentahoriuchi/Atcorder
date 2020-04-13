N,K = list(map(int, input().split()))
p = list(map(int, input().split()))
max_l = 0
Max_l = p[0:K]
S = [0]
s=0
for j in range(N):
    s += p[j]
    S.append(s)

for i in range(N-K+1):
    m = S[K+i]-S[i]
    if m > max_l:
        max_l = m



print((max_l+K)/2)
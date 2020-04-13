N = int(input())
S = list(input())
s_r = []
s_g = []
s_b = []

for i in range(len(S)):
    if S[i] == 'R':
        s_r.append(i)
    elif S[i] == 'G':
        s_g.append(i)
    elif S[i] == 'B':
        s_b.append(i)

N = len(s_r)*len(s_g)*len(s_b)

s_b = set(s_b)
for i in range(len(s_r)):
    for j in range(len(s_g)):
        M = max(s_r[i],s_g[j])
        m = min(s_r[i],s_g[j])
        if M+(M-m) in s_b:
            N -= 1

        if (M-m) %2 == 0:
            if m + (M-m)//2 in s_b:
                N -= 1

        if m-(M-m) in s_b:
            N -= 1

print(N)


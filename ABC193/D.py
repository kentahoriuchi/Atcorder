K = int(input())
S = list(input())
T = list(input())

def tokuten(s):
    t = [0]*9
    for i in range(len(s)):
        i = int(s[i])
        t[i-1] += 1
    ans = 0
    for k in range(len(t)):
        ans += (k+1) * 10 ** t[k]
    
    return ans

kard = [K]*9
for i in range(4):
    s = int(S[i])
    kard[s-1] -= 1
for i in range(4):
    t = int(T[i])
    kard[t-1] -= 1

bunbo = sum(kard)*(sum(kard)-1)
bunsi = 0


for i in range(1,10):
    for k in range(1,10):
        if i == k:
            if kard[i-1] <= 1:
                continue
        else:
            if kard[i-1] == 0 or kard[k-1] == 0:
                continue

        S[4] = i
        T[4] = k
        if tokuten(S) > tokuten(T):
            if i == k:
                bunsi +=  kard[i-1] * (kard[i-1]-1)
            else:
                bunsi += kard[i-1] * kard[k-1]

print(bunsi/bunbo)


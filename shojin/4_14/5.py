S = list(input())
acgt = ['A','C','G','T']
ans = 0

for i in range(len(S)):
    for j in range(len(S)-i):
        s = S[j:j+i+1]
        s = list(set(s))
        flag = True
        for t in s:
            if t not in acgt:
                flag = False
        if flag:
            ans = max(ans,i+1)

print(ans)


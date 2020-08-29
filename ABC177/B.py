S = input()
T = input()
ans = 1001

for i in range(len(S)-len(T)+1):
    s = 0
    for j in range(len(T)):
        if S[i+j] != T[j]:
            s += 1
    ans = min(ans,s)

print(ans)
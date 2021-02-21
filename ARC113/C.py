S = list(input())

S.reverse()
# S[]//97

string = [0]*26
pre = 27

ans = 0

for i in range(len(S)):
    alph = ord(S[i])%97
    # print(alph,pre)
    if pre == alph:
        ans += sum(string)-string[alph]
        string = [0]*26
        string[alph] += i

    string[alph] += 1
    # print(string)
    pre = alph

print(ans)



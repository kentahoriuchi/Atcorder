s = input()
ans = []

for i in range(len(s)):
    if s[i] == '0' or s[i] == '1':
        ans.append(s[i])
    else:
        if ans:
            _ = ans.pop()


print(''.join(ans))


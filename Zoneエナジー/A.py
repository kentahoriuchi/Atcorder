S = list(input())

ans = 0
for i in range(len(S)-3):
    if ''.join(S[i:i+4]) == 'ZONe':
        ans += 1

print(ans)
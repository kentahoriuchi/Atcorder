N = int(input())
S = []
count = 0
for _ in range(N):
    s = list(input())
    s.sort()
    S.append(s)

for i in range(N):
    for j in range(i+1,N):
        if S[i] == S[j]:
            count += 1

print(count)

N = int(input())
S = []
for _ in range(N):
    a = input()
    S.append(a)

set_S = set(S)

print(len(set_S))
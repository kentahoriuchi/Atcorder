N,K = list(map(int, input().split()))
R,S,P = list(map(int, input().split()))
T = list(input())
ans = 0

for i in range(N):
    if i >= K and T[i] == T[i-K]:
        T[i] = 'zero'

for l in range(N):
    if T[l] == 'r':
        ans += P
    elif T[l] == 's':
        ans += R
    elif T[l] == 'p':
        ans += S

print(ans)




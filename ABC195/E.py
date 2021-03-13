N = int(input())
S = list(input())
X = list(input())

S.reverse()
X.reverse()

dp = [[0 for _ in range(7)] for _ in range(N+1)]
dp[0][0] = 1
keta = 0

for i in range(N):
    if X[i] == 'A':
        for j in range(7):
            if dp[i][(j *10 + int(S[i])) % 7] == 1 and  dp[i][(j *10) % 7] == 1:
                dp[i+1][j] = 1
            else:
                dp[i+1][j] = 0
    elif X[i] == 'T':
        for j in range(7):
            if dp[i][(j *10 + int(S[i])) % 7] == 1 or  dp[i][(j *10) % 7] == 1:
                dp[i+1][j] = 1
            else:
                dp[i+1][j] = 0
# print(dp)
if dp[-1][0] == 1:
    print('Takahashi')
else:
    print('Aoki')
    
    
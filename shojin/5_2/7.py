n = int(input())
ans = []

for _ in range(n):
    X = input()
    Y = input()

    dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]

    for i in range(len(X)):
        for j in range(len(Y)):
            if X[i] == Y[j]:
                dp[i+1][j+1] = max(dp[i][j]+1,max(dp[i+1][j],dp[i][j+1]))
            else:
                dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

    ans.append(dp[len(X)][len(Y)])

for i in ans:
    print(i)

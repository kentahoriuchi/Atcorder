N,W = list(map(int, input().split()))
w_0 = []
w_1 = []
w_2 = []
w_3 = []
v = []
w = 0
w_count = [0]*4
for _ in range(N):
    a,b = list(map(int, input().split()))
    if w == 0:
        w = a
        w_0.append(b)
    else:
        if a == w:
            w_0.append(b)
        elif a == w+1:
            w_1.append(b)
        elif a == w+2:
            w_2.append(b)
        elif a == w+3:
            w_3.append(b)
    w_count[a-w] += 1

w_0.sort(reverse=True)
w_1.sort(reverse=True)
w_2.sort(reverse=True)
w_3.sort(reverse=True)
ans = 0

for i in range(w_count[0]+1):
    for j in range(w_count[1]+1):
        for k in range(w_count[2]+1):
            for l in range(w_count[3]+1):
                if W >= w * i + (w+1) * j + (w+2) * k + (w+3) * l:
                  
                    S = sum(w_0[:i])+sum(w_1[:j])+sum(w_2[:k])+sum(w_3[:l])
                    ans = max(ans,S)

print(ans)




# dp = [[0]*(W+1) for _ in range(N+1)]

# for i in range(N):
#     for j in range(W+1):
#         if j - w[i] < 0:
#             dp[i+1][j] = dp[i][j]
#         else:
#             dp[i+1][j] = max(dp[i][j],dp[i][j-w[i]] + v[i])

# k = max(dp)
# print(max(k))
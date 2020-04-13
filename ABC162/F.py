N = int(input())
A = list(map(int, input().split()))
inf = float('inf')
ans = -1 *inf

if N % 2 == 0:
    S_odd = [0]*(N//2+1)
    S_even = [0]*(N//2+1)
    s_odd = 0
    s_even = 0
    for i in range(len(A)):
        if i%2 == 0:
            s_odd += A[i]
            S_odd[i//2+1] = s_odd
        else:
            s_even += A[i]
            S_even[i//2+1] = s_even
    
    s = 0
    for j in range(N//2+1):
        s = S_odd[j] + S_even[N//2]-S_even[j] 
        ans = max(ans,s)
else:
    # S_odd = [0]*(N//2+2)
    # S_even = [0]*(N//2+1)
    # odd = []
    # even = []
    # s_odd = 0
    # s_even = 0
    # for i in range(len(A)):
    #     if i%2 == 0:
    #         s_odd += A[i]
    #         S_odd[i//2+1] = s_odd
    #         odd.append(A[i])
    #     else:
    #         s_even += A[i]
    #         S_even[i//2+1] = s_even
    #         even.append(A[i])
    
    # s = 0
    # ans = sum(odd)

    # for j in range(N//2):
    #     for k in range(j,N//2):
    #         s = S_odd[j] + S_even[k]-S_even[j] +S_odd[N//2+1]-S_odd[k+1]
    #         ans = max(ans,s)

    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1,N):
        for j in range((N-1)//2,(N+1)//2+1):
            dp[i+1][j] = max(dp[i][j],dp[i-1][j-1]+A[i])
    
    print(dp)
    print(dp[N][N//2])

print(ans)

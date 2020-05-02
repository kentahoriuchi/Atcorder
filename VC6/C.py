N,X,Y = list(map(int, input().split()))

ans = [0]*(N+1)

for i in range(1,N+1):
    for j in range(i+1,N+1):
        ans[min(j-i,abs(j-Y)+abs(i-X)+1)] += 1

for j in range(1,N):
    print(ans[j])


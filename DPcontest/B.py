N,K = list(map(int, input().split()))
h = list(map(int, input().split()))
d = [0] *N
d[1] = abs(h[1] - h[0])

for i in range(2,N):
    if i >= K:
        d[i] = min(d[i-j]+abs(h[i]-h[i-j]) for j in range(1,K+1))
    else:
        d[i] = min(d[i-j]+abs(h[i]-h[i-j]) for j in range(1,i+1))

print(d[-1])


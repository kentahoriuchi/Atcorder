N = int(input())
ans = 0

for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        x = N//i - 1
        if x > i:
            ans += x

print(ans)
N,A,B = list(map(int, input().split()))
s = 0

for i in range(1,N+1):
    k = i
    a = 0
    for l in range(len(str(i))):
        a += k%10
        k = int(k/10)
    if a >= A and a <= B:
        s += i

print(s)



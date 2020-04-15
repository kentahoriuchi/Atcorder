N,M = list(map(int, input().split()))

ans = 1

for i in range(2,100000):
    ans += i*((1-(1/(2**M)))**(i-1))

if int(ans*((N-M)*100+M*1900)/(2**M))%10 == 0:
    print(int(ans*((N-M)*100+M*1900)/(2**M)))
else:
    print(int(ans*((N-M)*100+M*1900)/(2**M))+1)


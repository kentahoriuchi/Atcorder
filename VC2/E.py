N,M = list(map(int, input().split()))
divi = []

for i in range(1,int(M**0.5)+1):
    if M % i == 0:
        if i >= N:
            divi.append(i)
        if i != M//i:
            if M//i >= N:
                divi.append(M//i)

print(M//min(divi))

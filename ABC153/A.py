H,A = list(map(int, input().split()))
i = 0
while(True):
    i += 1
    if A * i >= H:
        break

print(i)
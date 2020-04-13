H = int(input())
count = 0

while(True):
    if H == 1:
        break
    count += 1
    H = H//2

print(2**(count+1)-1)
n = int(input())
s = 0

if int(n/100) == 1:
    s += 1
if n%100 >= 10:
    s += 1
if n%10 == 1:
    s += 1

print(s)
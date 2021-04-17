from math import gcd
A,B = list(map(int, input().split()))

ans = 0
h = [0]*(B+1)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
for i in range(A,B+1):
    yaku = make_divisors(i)
    for j in yaku:
        h[j] += 1
# print(h)
h.reverse()
# print(h)
for k in range(len(h)):
    if h[k] >= 2:
        print(len(h)-k-1)
        break
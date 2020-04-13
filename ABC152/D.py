N = int(input())
count = 0

c = [[0 for i in range(10)]for j in range(10)]

for i in range(1,N+1):
    str_i = str(i)
    c[int(str_i[0])][int(str_i[-1])] += 1

for j in range(10):
    for k in range(10):
        count += c[j][k] * c[k][j]

print(count)



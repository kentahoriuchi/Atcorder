S = list(input())
count = 0

for i in range(int(len(S)/2)):
    if S.pop(0) != S.pop(-1):
        count += 1

print(count)
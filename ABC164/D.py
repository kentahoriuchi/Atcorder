S = input()
count = 0
l = [0]*2019
l[0] = 1
mod = 2019
tmp = 0

for i in range(1,len(S)+1):
    tmp = (tmp + int(S[len(S)-i])*pow(10,i-1,mod))%mod
    l[tmp] += 1
    

for j in range(2019):
    if l[j] >= 2:
        count += l[j]*(l[j]-1)//2

print(count)

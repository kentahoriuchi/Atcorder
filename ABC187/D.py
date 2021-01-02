N = int(input())
x = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    tmp.append(tmp[1]+2*tmp[0])
    x.append(tmp)
    # print(x)

x = sorted(x, key=lambda x: x[2],reverse=True)
# print(sortedx)

taka = [0]*N
ao = [0]*N
for i in range(N):
    taka[i] = x[i][1]
    ao[i] = x[i][0]

taka_S = 0
ao_S = sum(ao)

if taka_S > ao_S:
    print(0)

else:
    # ao.sort(reverse=True)
    ans = 0
    for i in range(N):
        taka_S += ao[i] + taka[i]
        ao_S -= ao[i]
        ans += 1
        if taka_S > ao_S:
            print(ans)
            break
from itertools import permutations
N = int(input())
r = []
for _ in range(N):
    r.append(list(map(int, input().split())))

def naname(l):
    masu = []
    now = [l[0],l[1]]
    while now[0] >= 1 and now[1] >= 1:
        masu.append([now[0]-1,now[1]-1])
        now = [now[0]-1,now[1]-1]
    now = [l[0],l[1]]
    while now[0] >= 1 and now[1] <= 6:
        masu.append([now[0]-1,now[1]+1])
        now = [now[0]-1,now[1]+1]
    now = [l[0],l[1]]
    while now[0] <= 6 and now[1] >= 1:
        masu.append([now[0]+1,now[1]-1])
        now = [now[0]+1,now[1]-1]
    now = [l[0],l[1]]
    while now[0] <= 6 and now[1] <= 6:
        masu.append([now[0]+1,now[1]+1])
        now = [now[0]+1,now[1]+1]
    return masu

li=list(range(8))
remo = []
koma = []
kiki = []
for i in range(len(r)):
    li.remove(r[i][1])
    remo.append(r[i][0])
    koma.append(r[i])
    kiki.extend(naname(r[i]))

per=permutations(li,len(li))
for i in per:
    i = list(i)
    tmp_koma = [x for x in koma]
    tmp_kiki = [x for x in kiki]
    count = 0
    for j in range(8):
        if j in remo:
            continue
        else:
            if [j,i[count]] in tmp_kiki:
                break
            else:
                tmp_koma.append([j,i[count]])
                tmp_kiki.extend(naname([j,i[count]]))
                count += 1
    if len(tmp_koma) == 8:
        koma = [x for x in tmp_koma]
        break

koma.sort()
pr = list('........')
for k in range(8):
    p = [x for x in pr]
    p[koma[k][1]] = 'Q'
    print(''.join(p))









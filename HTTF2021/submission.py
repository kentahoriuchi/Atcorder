init = []
for _ in range(100):
    init.append(list(map(int, input().split())))

pos = [0,0]
# order = []

def idou(pos,target):
    return [(pos[0]-target[0]),(pos[1]-target[1])]

def path(ido,pos):
    posisions = []
    re = []
    for i in range(abs(ido[0])+abs(ido[1])):
        if ido[0]>0:
            re.append('U')
            ido = [ido[0]-1,ido[1]]
            posisions.append([pos[0]-1,pos[1]])
            pos = [pos[0]-1,pos[1]]
        elif ido[0]<0:
            re.append('D')
            ido = [ido[0]+1,ido[1]]
            posisions.append([pos[0]+1,pos[1]])
            pos = [pos[0]+1,pos[1]]
        else:
            if ido[1]>0:
                re.append('L')
                ido = [ido[0],ido[1]-1]
                posisions.append([pos[0],pos[1]-1])
                pos = [pos[0],pos[1]-1]
            elif ido[1]<0:
                re.append('R')
                ido = [ido[0],ido[1]+1]
                posisions.append([pos[0],pos[1]+1])
                pos = [pos[0],pos[1]+1]
    return posisions,re


def alpha(idou):
    re = ''
    if idou[0]>=0:
        re += 'U'*idou[0]
    elif idou[0]<0:
        re += 'D'*abs(idou[0])
    if idou[1]>=0:
        re += 'L'*idou[1]
    elif idou[1]<0:
        re += 'R'*abs(idou[1])
    return re

def idou_alph(idou,pos):
    if idou[0]>0:
        return 'U',[idou[0]-1,idou[1]],[pos[0]+1,pos[1]]
    elif idou[0]<0:
        return 'D',[idou[0]+1,idou[1]],[pos[0]-1,pos[1]]
    else:
        if idou[1]>0:
            return 'L',[idou[0],idou[1]-1],[pos[0],pos[1]+1]
        elif idou[1]<0:
            return 'R',[idou[0],idou[1]+1],[pos[0],pos[1]-1]
        else:
            return 0

def distance(pos,target):
    return (abs(pos[0]-target[0])+abs(pos[1]-target[1]))

def simple(init):
    simple_ans = []
    pos = [0,0]
    for p in (init):
        ido = idou(pos,p)
        simple_ans.append(alpha(ido))
        simple_ans.append('I')
        pos = p
    ans = ''.join(simple_ans)
    return ans, len(ans)-100

order = []
for i in range(len(init)):
    p = init[i]
    ido = idou(pos,p)
    have = False
    pre_pos = [0,0]
    pat,an = path(ido,pos)
    ind = 0
    # print(pat)
    pos = pat[-1]
    blank = len(pat)
    ins = 0
    for zahyou in pat:
        if zahyou in init:
            blank -= 1
    for z in range(len(pat)):
        zahyou = pat[z]
        if have:
            if blank == 0:
                an.insert(z+ins,'O')
                ins += 1
                init[ind] = pre_pos
                have = False
            elif distance(pre_pos,init[ind+1]) <= distance(zahyou,init[ind+1]) and pre_pos in init:
                an.insert(z+ins,'O')
                ins += 1
                init[ind] = pre_pos
                have = False
            else:
                pre_pos = zahyou
        # print(zahyou)
        if not have and blank != 0:
            if zahyou in init:
                pre_pos = zahyou
                ind = init.index(zahyou)
                have = True
                an.insert(z+1+ins,'I')
                ins += 1
        elif not zahyou in init:
            blank -= 1
    an.append('I')
    order.extend(an)

ans = ''.join(order)
print(ans)
        

    


# ord,num = simple(init)
# print(ord)

# print(path([6,15],[0,0]))

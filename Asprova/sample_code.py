#Header read

_,H = input().split()
M,I,R,BL,CL = list(map(int, H))

# M = パン焼き器番号
# I = パン種類
# R = オーダー数
# BL = BOM(機器情報)行数
# CL = COMBI(段取り)行数

#Machine read

rq = [0]*M
mn = [0]*M
md = []

for i in range(M):
    _,machine = input().split()
    machine = list(map(int, machine))
    m = machine[0]
    rq[m] = machine[1]
    mn[m] = machine[2]
    md.append(mathine[2:])

# rq = 焼ける数
# mn = 休日の個数
# md[] = 休日データ

#BOM read

inf = float('inf')
c = [[inf]*M for _ in range(I)]
ec = [[inf]*M for _ in range(I)]

for i in range(BL):
    _,bom = input().split()
    bom = list(map(int, bom))
    c[bom[0]][bom[1]] = bom[2]
    ec[bom[0]][bom[1]] = bom[3]

# c[][] = パンの焼き時間
# ec[][] = 電力コスト
#[パンの種類][マシン番号]

#COMBI read

inf = float('inf')
c = [[[inf]*I for _ in range(I)] for _ in range(M)]
ec = [[[inf]*I for _ in range(I)] for _ in range(M)]

for i in range(BL):
    _,combi = input().split()
    combi = list(map(int, combi))
    t[combi[0]][combi[1]][combi[2]] = combi[3]
    cc[combi[0]][combi[1]][combi[2]] = combi[4]

# t[][] = パン切り替えにかかる時間
# cc[][] = 段取りコスト
# [マシン番号][切り替え前のパン][切り替え後のパン]
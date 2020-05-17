import math
A,B,H,M= list(map(int, input().split()))

bx = B * math.sin(M/60*2*math.pi)
by = B * math.cos(M/60*2*math.pi)
ax = A * math.sin((H/12+M/720)*2*math.pi)
ay = A * math.cos((H/12+M/720)*2*math.pi)

print(math.sqrt((ax-bx)**2+(ay-by)**2))

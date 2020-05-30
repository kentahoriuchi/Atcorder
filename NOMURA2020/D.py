N = int(input())
P = list(map(int, input().split()))
mod = 10**9+7

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
      self.par = [i for i in range(n+1)]
      self.rank = [0] * (n+1)
    
    def same_check(self, x, y):
      return self.find(x) == self.find(y)
    
    def find(self, x):
      # 根ならその番号を返す
      if self.par[x] == x:
        return x
        # 根でないなら、親の要素で再検索
      else:
        self.par[x] = self.find(self.par[x])
        return self.find(self.par[x])
    def union(self, x, y):
      # 根を探す
      x = self.find(x)
      y = self.find(y)
      if self.rank[x] < self.rank[y]:
          self.par[x] = y
      else:
          self.par[y] = x
          if self.rank[x] == self.rank[y]:
              self.rank[x] += 1

uf = UnionFind(N)
yet = []
for i in range(N):
  if P[i] != -1:
    uf.union(i+1,P[i])
  else:
    yet.append(i+1)

print(uf.par)

r = [0]*(N+1)
l = [0]*(N+1)
for j in range(N):
  if r[uf.par[j]]==0:
    l[j] += 1
  r[uf.par[j]] += 1

route_base = sum(r)-sum(l[1:])

ans = 1
for youso in yet:
  con = uf.par.count(uf.par[yet])
  c = N - con
  

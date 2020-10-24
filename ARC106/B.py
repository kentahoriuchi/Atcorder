N,M = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

 
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            st = []
            while self.parents[x] >= 0:
                st.append(x)
                x = self.parents[x]
            for y in st:
                self.parents[y] = x
            return x
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        group = {r:[] for r in self.roots()}
        for i in range(self.n):
            group[self.find(i)].append(i)
        return group
 
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
 
 
uf = UnionFind(N)
for i in range(M):
    c,d = list(map(int, input().split()))
    uf.union(c-1,d-1)
 
u = list(uf.all_group_members().values())
for j in u:
    sa = 0
    sb = 0
    for k in j:
        sa += a[k]
        sb += b[k]
    if sa != sb:
        print('No')
        exit()
print('Yes')
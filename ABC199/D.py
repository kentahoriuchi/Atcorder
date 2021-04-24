import sys
N,M = list(map(int, input().split()))
A = []
path = [[0]*N for i in range(N)]
for _ in range(M):
    a = list(map(int, input().split()))
    A.append(a)
    path[a[0]-1][a[1]-1] += 1
    path[a[1]-1][a[0]-1] += 1


# print(path)
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

uf = UnionFind(N)
for i in range(M):
    uf.union(A[i][0]-1,A[i][1]-1)

check = [0]*N

ans = 1
for i in range(N):
    if check[i] == 1:
        continue
    else:
        m = uf.members(i)
        if len(m) == 1:
            ans *= 3
            continue
        l = [0]*len(m)
        for k in range(len(m)):
            l[k] = sum(path[k])
            if sum(path[k]) >= 3:
                print(0)
                sys.exit()
            check[k] = 1
        count = 0
        for r in l:
            if r == 1:
                count += 1
        if count == 0:
            if len(m)%3 != 0:
                print(0)
                sys.exit()
            else:
                ans *= 6
        
        else:
            ans *= 3*2**(len(m)-1)
print(ans)



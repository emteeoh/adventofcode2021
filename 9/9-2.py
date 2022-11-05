from collections import defaultdict
import copy


# noinspection SpellCheckingInspection
class Matrix:
    def __init__(self):
        self.m = []
        self.maxx = -1
        self.maxy = -1

    def resize(self, p):
        try:
            if self.maxx < p.x:
                delta = p.x - self.maxx
                self.maxx = p.x
                # print("before X extend", self.m, p)
                self.m.extend([[0] * (self.maxy + 1)] * delta)
                # print("after X extend", self.m, p, self.maxx, self.maxy)
            if self.maxy < p.y:
                for i in self.m:
                    delta = p.y - self.maxy
                    self.maxy = p.y
                    # print("before Y extend", self.m, p)
                    i.extend([0]*delta)
                    # print("before Y extend", self.m, p)
        except AttributeError:
            print("p should be type Points")
            raise AttributeError

    def __setitem__(self, p, v):
        self.resize(p)
        try:
            self.m[p.x][p.y] = v
        except IndexError:
            print("IndexError:")
            print("point", p)
            print("matrix", self.m)
            print("maxx", self.maxx, "maxy", self.maxy)
            raise

    def __str__(self):
        s = ""
        for ll in self.m:
            for cc in ll:
                s += f"{cc}"
            s += "\n"
        return s

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, p):
        self.resize(p)
        return self.m[p.x][p.y]

    def adjacents(self, p):
        return [Points(a, b) for a, b in
                [(p.x - 1, p.y), (p.x + 1, p.y), (p.x, p.y - 1), (p.x, p.y + 1)] if
                a in range(self.maxx+1) and (b in range(self.maxy+1))]

    def __len__(self):
        return (self.maxx + 1)*(self.maxy + 1)

    def __iter__(self):
        return MatrixIter(self)


class MatrixIter:
    def __init__(self,m):
        self.m = m
        self.p = Points(0,0)

    def __next__(self):
        if self.p.x <= self.m.maxx:
            q = self.p.copy()
            self.p.y += 1
            if self.p.y > self.m.maxy:
                self.p.y = 0
                self.p.x += 1
            return q
        else:
            raise StopIteration


# noinspection SpellCheckingInspection
class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Points({self.x}, {self.y})"

    def __eq__(self, y):
        return (self.x == y.x ) and (self.y == y.y)

    def copy(self):
        return Points(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))


fname = "input.txt"
grid = Matrix()
with open(fname) as file:
    for r, row in enumerate(file):
        for c, col in enumerate(row.strip()):
            grid[Points(r, c)] = int(col)

# Part One
# print(grid)
# find lows
lows = []
for j in grid:
    l = True
    for a in grid.adjacents(j):
        if grid[a] <= grid[j]:
            l = False
    if l:
        lows.append(j)

risks={}
totalRisk = 0
for j in lows:
    risks[j] = 1 + grid[j]
    totalRisk += risks[j]
print(f"risk {totalRisk}")

#Part Two

def floodABasin(p):
    b=set([p])
    while True:
        change = False
        bb = copy.copy(b)
        for p in bb:
            n = grid.adjacents(p)
            for nn in n:
                if grid[nn] != 9:
                    if nn not in b:
                        b.add(nn)
                        change = True
        if not change:
            break
    return b


basins = defaultdict(set)
bc = 0
for l in lows:
    b = floodABasin(l)
    if b not in basins.values():
        basins[bc] = b
        bc += 1

sizes = [ (o,len(p))  for o,p in basins.items() ]
sizes.sort(key=lambda o: o[1])
print(sizes[-3:])
bbb = 1
for s in sizes[-3:]:
    bbb *= s[1]
print(bbb)
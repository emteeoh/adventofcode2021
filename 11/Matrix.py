class Matrix:
    def __init__(self):
        self.m = []
        self.maxx = -1
        self.maxy = -1

    def _resize(self, p):
        try:
            # print(f"resize: {p} max: {self.maxx} {self.maxy}")
            if self.maxy < p.y:
                delta = p.y - self.maxy
                self.maxy = p.y
                # print("before Y extend", self.m, p)
                self.m.extend([[0] * (self.maxx + 1)] * delta)
                # print(f"after Y extend Matrix: {self.m}  {p}  max: {self.maxx}, {self.maxy}")
            if self.maxx < p.x:
                delta = p.x - self.maxx
                self.maxx = p.x
                for i in self.m:
                    # print("before Y extend", self.m, p)
                    i.extend([0]*delta)
                # print(f"after X extend Matrix: {self.m}  {p}  max: {self.maxx}, {self.maxy}")
        except AttributeError:
            print("p should be type Points")
            raise AttributeError

    def __setitem__(self, p, v):
        self._resize(p)
        try:
            self.m[p.y][p.x] = v
        except IndexError:
            print("IndexError:")
            print("point", p.x, p.y)
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
        self._resize(p)
        return self.m[p.y][p.x]

    def adjacents(self, p):
        return [Points(a, b) for a, b in
                [(p.x - 1, p.y), (p.x + 1, p.y), (p.x, p.y - 1), (p.x, p.y + 1)] if
                a in range(self.maxx+1) and (b in range(self.maxy+1))]

    def cardinalAdjacents(self,p):
        return self.adjacents(p)

    def ordinalAdjacents(self, p):
        return [Points(a, b) for a, b in
                [(p.x-1, p.y-1), (p.x, p.y-1), (p.x+1, p.y-1),
                (p.x-1, p.y), (p.x, p.y), (p.x+1, p.y),
                (p.x-1, p.y+1), (p.x, p.y+1), (p.x+1, p.y+1)] if a in range(self.maxx+1) and (b in range(self.maxy+1))]

    def __len__(self):
        return (self.maxx + 1)*(self.maxy + 1)

    def __iter__(self):
        return MatrixIter(self)

    def __len__(self):
        return (self.maxx + 1) * (self.maxy + 1)


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


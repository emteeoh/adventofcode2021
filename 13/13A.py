
class Grid:
    def __init__(self):
        self.points = set()
        self.maxx = 0
        self.maxy = 0

    def __repr__(self):
        return f"Max: {self.maxx} {self.maxy} Points {self.points}"

    def __str__(self):
        l = list(" "*(self.maxx+1)*(self.maxy+1))
        s=""
        for p in self.points:
            l[p[0]+(self.maxx+1)*p[1]] = '#'
        for i in range(self.maxy+1):
            for j in range(self.maxx+1):
                s += l[j+i*(self.maxx+1)]
            s += '\n'
        s += f'Max x:{self.maxx} y:{self.maxy}\nLength: {len(self.points)}'
        return s

    def findmax(self):
        self.maxx = self.maxy = 0
        for p in self.points:
            self.maxx = max(self.maxx, p[0])
            self.maxy = max(self.maxy, p[1])


    def addDot(self,dot):
        x, y = (int(i) for i in dot.split(",") )
        self.points.add((x,y))
        self.maxx = max(self.maxx, x)
        self.maxy = max(self.maxy, y)

    def __len__(self):
        return len(self.points)

    def foldVertical(self,y):
        halfPoints = set()
        for point in self.points:
            if point[1] < y:
                halfPoints.add(point)
            elif point[1] > y:
                halfPoints.add((point[0], (2*y) - point[1]))
        self.points = halfPoints
        self.findmax()


    def foldHorizontal(self,x):
        halfPoints = set()
        for point in self.points:
            if point[0] < x:
                halfPoints.add(point)
            elif point[0] > x:
                halfPoints.add(((2*x) - point[0], point[1]))
        self.points = halfPoints
        self.findmax()

    def save(self,fname):
        with open(fname,"w") as sfile:
            for p in self.points:
                sfile.write(f"{p[0]},{p[1]}\n")




grid= Grid()
fold = []
fname = "sample.txt"
iteration = 0
with open(fname) as infile:
    foldrules = False
    for line in infile:
        l = line.strip()
        if l:
            if not foldrules:
                grid.addDot(l)
            else:
                a,c = l.removeprefix("fold along ").split("=")
                if a == 'x':
                    grid.foldHorizontal(int(c))
                else:
                    grid.foldVertical(int(c))
        else:
            foldrules = True
    if foldrules:
            iteration += 1

print(grid)


from Matrix import Matrix, Points


def incPoint(g, pp, fp):
    f = 0
    grid[pp] += 1
    if grid[pp] > 9 and pp not in fp:
        # print(f"{pp} flashes")
        fp.append(pp)
        f = 1
        for ii in g.ordinalAdjacents(pp):
            # print(f"working on adjacent {ii} of {pp}")
            f += incPoint(g, ii, fp)
            # print(f"done adjacent {ii} of {pp}")
    return f

def simOneRound(g,fp):
    f = 0
    for pp in grid:
        f += incPoint(grid, pp, fp)
    return f

def resetGrid(g):
    for pp in g:
        if g[pp] > 9:
            g[pp] = 0


grid = Matrix()
fname = "input.txt"
x = y = 0
with open(fname) as file:
    for line in file:
        for c in line.strip():
            # print(Points(x, y), c)
            grid[Points(x, y)] = int(c)
            x += 1
        x = 0
        y += 1
print(grid)
flashCount = 0
firstSync = False
step = 0
while not firstSync:
    flashPoints = []
    flashCount += simOneRound(grid,flashPoints)
    resetGrid(grid)
    if len(flashPoints) == len(grid):
        firstSync = True
    step += 1
print()
# print(grid)
print(f"{step}")
# print(f"{flashCount}")
# answer 1971 is too high


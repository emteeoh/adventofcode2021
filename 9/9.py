from collections import defaultdict


def risk(h):
    return 1+h

def listAdjacents(x, y):
    return [[a,b] for a,b in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if (a in range(maxr)) and (b in range(maxc))]


def checklowest(g, x, y):
    adjacents = listAdjacents(x, y)
    # print(x,y,adjacents)
    for a,b in adjacents:
        # print(a,b, x, y,  end='')
        # print(' ',g[x][y], end='')
        # print(' ', g[a][b])
        if g[a][b] <= g[x][y]:
            return False
    return True

def visit(p, i):
    x, y = p
    o = []
    adjacents = listAdjacents(x, y)
    for a,b in adjacents:
        if basins[a][b] != -1:
            continue
        if grid[a][b] == 9:
            continue
        basins[a][b] = i
        o.append([(a,b),i])

def greedyBasin(b):
    for p in l:
        for n in listAdjacents(p):







grid=defaultdict(list)
with open("sample.txt") as file:
    for r, row in enumerate(file):
        for c,col in enumerate(row.strip()):
            grid[r].append(int(col))

maxc =  len(grid[0])
maxr = len(grid)
print(f"rows: {maxr}  columns: {maxc}")
sum = 0
lowpoints = []
for i in range(0,maxr):
    for j in range(0,maxc):
        if checklowest(grid,i,j):
            # print('hit! ', i, j, grid[i][j])
            lowpoints.append((i,j))
            sum += risk(grid[i][j])

basins = []
for i, p in enumerate(lowpoints):
    basins.append(set(p))

for b in basins:
    greedybasin(b)


print(sum)

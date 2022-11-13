import graph
from collections import Counter


def isOkPath(p):
    if p[0] != 'start':
        return False
    if p[-1] == 'end':
        return True
    if p[-1] == 'start' and len(p) > 1:
        return False
    if p[-1].isupper():
        return True
    counts = Counter()
    for e in p:
        if e.islower():
            counts[e] += 1
    if max(counts.values()) > 2:
        return False
    m = counts.most_common(2)
    if len(m) == 2 and m[1][1] == 2:
        return False
    else:
        return True


def walk(gg, path, visit, spacing=""):
    # print(f"Walk {path} {visit} {gg}")
    if visit == 'end':
        return [path+['end']]
    else:
        if isOkPath(path+[visit]):
            p = []
            n = gg.getNeighbors(visit)
            for e in n:
                r = walk(gg, path+[visit], e, spacing+" ")
                if r:
                    p.extend(r)
            return p


g = graph.Graph()
fname1 = "input.txt"
fname2 = "sampleS-result.txt"
with open(fname1) as file:
    for line in file:
        i, j = line.strip().split('-')
        g.addNode(i)
        g.addNode(j)
        g.addLink(i, j)
paths = walk(g, [], "start")
print(f"{len(paths)}")

# for singlePath in paths:
#     print(singlePath)

# paths2 = []
# with open(fname2) as file:
#     for line in file:
#         paths2.append(line.strip().split(','))
# m = [a for a in paths2 if a not in paths]
# e = [a for a in paths if a not in paths2]
# print(f"missing from mine: {len(m)}")
# print(f"extras mine: {len(e)}")
#
# print(m)
#
# print(e)
# 326817 is too high
# 5457 is too low
# 128506 correct

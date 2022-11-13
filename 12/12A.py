import graph


def bfs(gg, startv, visited, spacing=""):
    paths = []
    v = list(visited)
    if startv == 'end':
        # print(f"{spacing}End")
        return [["end"]]
    else:
        # print(f"{spacing}vertex {startv}\n{spacing}visited {visited}")
        n = gg.getNeighbors(startv)
        # print(f"{spacing}{startv} -> {n}")
        tovisit = []
        for e in n:
            if e not in v:
                tovisit.append(e)
        if startv.islower():
            v.append(startv)
        # print(f"{spacing}{startv} {n} {tovisit} {visited}")
        # print(f"{spacing}tovisit {tovisit}")
        for e in tovisit:
            # print(f"{spacing}{startv}->{e}")
            r = bfs(gg, e, v, spacing+" ")
            # print(f"{spacing}{startv} {r}")
            for rr in r:
                t = [startv]
                t.extend(rr)
                # print(f"{spacing}{t} {v}")
                paths.append(t)
        # print(f"{spacing}{paths}")
        return paths


g = graph.Graph()
fname = "input.txt"
with open(fname) as file:
    for line in file:
        i, j = line.strip().split('-')
        g.addNode(i)
        g.addNode(j)
        g.addLink(i, j)
        print(f"{i} -> {j}")

print(g.vertexes)
print(g.links)
print()

paths = bfs(g, 'start', [], '')
# for ip in paths:
#     print(ip)
print(len(paths))



class Graph:
    def __init__(self):
        self.vertexes = set()
        self.links = []

    def addNode(self, a):
        self.vertexes.add(a)

    def addLink(self, a, b):
        if (a in self.vertexes) and (b in self.vertexes) and ({a, b} not in self.links):
            self.links.append({a, b})

    def getNeighbors(self, a):
        n = []
        for i in self.links:
            if a in i:
                n.append(list(i - {a})[0])
        assert a not in n
        return n


if __name__ == "__main__":
    g = Graph()
    g.addNode("start")
    g.addNode("a")
    g.addNode("b")
    g.addNode("c")
    g.addNode("d")
    g.addNode("end")

    g.addLink("start", "a")
    g.addLink("start", "b")
    g.addLink("a", "c")
    g.addLink("a", "b")
    g.addLink("b", "d")
    g.addLink("a", "end")
    g.addLink("b", "end")

    print(g.vertexes)
    print(g.links)
    print(f" Start neighbors: {g.getNeighbors('start')}")
    print(f" A neighbors: {g.getNeighbors('a')}")
    print(f" B neighbors: {g.getNeighbors('b')}")
    print(f" C neighbors: {g.getNeighbors('c')}")
    print(f" D neighbors: {g.getNeighbors('d')}")
    print(f" end neighbors: {g.getNeighbors('end')}")

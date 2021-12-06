
def zip_longest_repeating(*iterables):
    iters = [iter(i) for i in iterables]
    sentinel = object()
    vals = tuple(next(it, sentinel) for it in iters)
    if any(val is sentinel for val in vals):
        return
    yield vals
    while True:
        cache = vals
        vals = tuple(next(it, sentinel) for it in iters)
        if all(val is sentinel for val in vals):
            return
        vals = tuple(old if new is sentinel else new for old, new in zip(cache, vals))
        yield vals


segments = []
with open("5Ainput.txt") as f:
    for line in f:
        segment = [int(item) for sublist in [ x.split(",") for x in line.rstrip().split(" -> ") ] for item in sublist]
        segments.append(segment)
grid = {}
for segment in segments:
    xstep = 1
    if segment[0] > segment[2]:
        xstep = -1
    ystep = 1
    if segment[1] > segment[3]:
        ystep = -1
    xiter = range(segment[0], segment[2]+xstep, xstep)
    yiter = range(segment[1], segment[3]+ystep, ystep)
    for x, y in zip_longest_repeating(xiter, yiter):
            try:
                grid[(x, y)] += 1
            except KeyError:
                grid[(x, y)] = 1

solution=0
for k,v in grid.items():
    if v >1 :
        solution += 1
print(solution, len(grid))


from collections import Counter

def polymerTemplateGen(pt):
    for c in pt:
        yield c


def transformGen(pt, rules, count):
    if count == 1:
        lgen = polymerTemplateGen(pt)
    else:
        lgen = transformGen(pt, rules, count - 1)
    left = next(lgen)
    while True:
        try:
            right = next(lgen)
        except StopIteration:
            break
        yield left
        yield rules[left+right]
        left = right
    yield right


infile = "sample.txt"
pairRules = dict()
with open(infile) as file:
    polymerTemplate = file.readline().strip()
    file.readline() # discard blank line
    for r in file:
        k,v = r.strip().split(" -> ")
        pairRules[k] = v

c = Counter()
for i in transformGen(polymerTemplate, pairRules, 40):
    c[i] += 1
m = c.most_common()
print(m)
print(m[0][1] - m[-1][1])

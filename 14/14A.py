from collections import Counter
import timeit

counter = Counter()


def polymerTemplateGen(pt):
    for c in pt:
        counter[c] += 1
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
        counter[rules[left+right]] += 1
        yield rules[left+right]
        left = right
    yield right

def go(steps, pt, r):
    for i in transformGen(pt, r, steps):
        continue


infile = "sample.txt"
pairRules = dict()
with open(infile) as file:
    polymerTemplate = file.readline().strip()
    file.readline()  # discard blank line
    for r in file:
        k,v = r.strip().split(" -> ")
        pairRules[k] = v

# cc = 0
# steps = 30
# for i in transformGen(polymerTemplate, pairRules, steps):
#     cc += 1

steps = 22
print(timeit.timeit(stmt='go(steps, polymerTemplate, pairRules)', globals=globals(), number=1))
m = counter.most_common()
print(f"counter dictionary: {m}")
print(f"most-least = {m[0][1] - m[-1][1]}")
# print(f"length of polymer: {cc}")
print(f"steps: {steps}")
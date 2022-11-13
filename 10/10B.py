

# stack
class Stack:
    def __init__(self):
        self.s = []

    def __iter__(self):
        return self

    def __next__(self):
        try:
            n = self.pop()
        except IndexError:
            raise StopIteration
        else:
            return n

    def push(self,a):
        self.s.append(a)

    def pop(self):
        return self.s.pop()

    def dump(self):
        self.s = []


opens = '([{<'
closes = ')]}>'
isMatch = lambda o, c: (opens.index(o) == closes.index(c))
getMatch = lambda o: closes[opens.index(o)]
points = { ')': 1, ']': 2, '}': 3, '>': 4}

# load file
input = "inputA.txt"
stack = Stack()
incompletes = []
scores = []
with open(input) as fname:
    # iterate over line
    for l in fname:
        discard = False
        for ch in l:
            # push opens ({[<
            if ch in opens:
                stack.push(ch)
            if ch in closes:
                # it's a close
                cc = stack.pop()
                # check for illegal close
                if not isMatch(cc, ch) :
                    discard = True
                    stack.dump()
                    break
        if not discard:
            fixes = ""
            score = 0
            for cc in stack:
                fixes += getMatch(cc)
                score = score * 5 + points[getMatch(cc)]
            # incompletes.append(l+fixes)
            # print(l, "  adding ", fixes, score)
            scores.append(score)
scores.sort()
print(scores)
print(scores[len(scores)//2])

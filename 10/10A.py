

# stack
class Stack:
    def __init__(self):
        self.s=[]

    def push(self,a):
        self.s.append(a)

    def pop(self):
        return self.s.pop()

opens = '([{<'
closes = ')]}>'
matches = lambda o,c: (opens.index(o)==closes.index(c))
points = { ')': 3, ']': 57, '}': 1197, '>': 25137}
# load file
input = "inputA.txt"
stack=Stack()
score = 0
with open(input) as fname:
    # iterate over line
    for l in fname:
        for ch in l:
            # push opens ({[<
            if ch in opens:
                stack.push(ch)
            if ch in closes:
                # it's a close
                cc = stack.pop()
                # check for illegal close
                if not matches(cc,ch) :
                    score += points[ch]
                    break

print(score)

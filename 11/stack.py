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

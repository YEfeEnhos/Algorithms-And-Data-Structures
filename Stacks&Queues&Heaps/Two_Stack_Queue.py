class TwoStackQueue():
    def __init__(self):
        self.instack = []
        self.outstack = []
    def enqueue(self, item):
        self.instack.append(item)
        self.outstack.append(item)
    def dequeue(self):
        return self.outstack.pop(0)
    
q = TwoStackQueue()

q.enqueue("C")
q.enqueue(2)
q.enqueue("A")

print(q.dequeue()) # print C
print(q.dequeue()) # print 2
print(q.dequeue()) # print A